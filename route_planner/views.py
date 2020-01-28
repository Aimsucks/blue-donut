import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from eve_esi import ESI
from eve_auth.models import EveUser

from route_planner.backend import RoutePlannerBackend
from eve_sde.models import SolarSystems

from networkx import NodeNotFound


class PlannerView(LoginRequiredMixin, View):
    """
    See if the following will work to clean up some of the code.

    def __init__(self):
        self.recents = RoutePlannerBackend().getInfo(request.user, 'recents')
        self.favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
    """
    def get(self, request):
        recents = RoutePlannerBackend().getInfo(request.user, "recents")
        favorites = RoutePlannerBackend().getInfo(request.user, "favorites")
        return render(request, "route_planner/planner.html",
                      {"recents": recents,
                       "favorites": favorites})

    def post(self, request):
        try:
            character = request.user.characters.get(character_id=int(request.POST['character_id']))
        except EveUser.DoesNotExist:
            return HttpResponse(status=403)

        RoutePlannerBackend().check_alliance(character)

        # Get character's current location from ESI
        req = ESI.request(
            'get_characters_character_id_location',
            client=character.get_client(),
            character_id=int(request.POST['character_id'])
        ).data.solar_system_id

        source_name = SolarSystems.objects.get(solarSystemID=req).solarSystemName

        # Error checking for characters in wormholes
        if re.match('J[0-9]{6}', source_name) or source_name == "Thera":
            return self.render_page(request, True, None, False, False, source_name, "wormhole")

        # Generate the route
        try:
            route = RoutePlannerBackend().generate(req, request.POST['destination'])
        except NodeNotFound or AttributeError or ObjectDoesNotExist:
            return self.render_page(request, True, None, False, False, source_name, "route")

        # Clicking the "Verify" button shows a map and a confirm route button
        if 'verify' in request.POST:
            return self.render_page(request, False, route, True, True)

        # Confirming the route after clicking "Verify"
        elif 'confirm' in request.POST:
            RoutePlannerBackend().updateRecents(request.user, request.POST['destination'])
            self.generate_route(character, route)
            return self.render_page(request, False, route, True, False)

        # Basically skipping having to click the "Confirm" button
        elif 'generate' in request.POST:
            RoutePlannerBackend().updateRecents(request.user, request.POST['destination'])
            self.generate_route(character, route)
            return self.render_page(request, False, route, True, False)

        # Clicking one of the "Favorites", "Recent", or "Popular" buttons
        else:
            RoutePlannerBackend().updateRecents(request.user, request.POST['destination'])
            self.generate_route(character, route)
            return self.render_page(request, False, route, True, False)

    def render_page(self, request, error, route, map_bool, confirm_bool, source_name=False, message=None):

        # Grab recents and favorites from database
        recents = RoutePlannerBackend().getInfo(request.user, "recents")
        favorites = RoutePlannerBackend().getInfo(request.user, "favorites")

        if error:
            if message == "wormhole":
                message = "You cannot generate a route from a wormhole. Try forcing a session change."
            elif message == "route":
                message = "Route generation failed. Please join Discord for help."

            return render(request, 'route_planner/error.html', {
                'recents': recents,
                'favorites': favorites,
                'mapDisplay': map_bool,
                'system': source_name,
                'message': message})
        else:
            return render(request, "route_planner/planner.html", {
                "recents": recents,
                "favorites": favorites,
                'dotlan': route['dotlan'],
                'destination': request.POST['destination'],
                'jumps': route['length'],
                'mapDisplay': map_bool,
                'confirmButton': confirm_bool})

    def generate_route(self, character, route):
        for i in range(len(route['esi'])):
            if i == 0:
                ESI.request(
                    'post_ui_autopilot_waypoint',
                    client=character.get_client(),
                    add_to_beginning=False,
                    clear_other_waypoints=True,
                    destination_id=route['esi'][i]
                )
            else:
                ESI.request(
                    'post_ui_autopilot_waypoint',
                    client=character.get_client(),
                    add_to_beginning=False,
                    clear_other_waypoints=False,
                    destination_id=route['esi'][i]
                )

class SystemView(LoginRequiredMixin, View):
    def get(self, request, system):
        return render(request, 'route_planner/system.html', {'system': system})


class EditView(LoginRequiredMixin, View):
    def get(self, request):
        favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
        return render(request, 'route_planner/favorites.html',
                      {'favorites': favorites})

    def post(self, request):
        favorites = request.POST.getlist('favorites')
        RoutePlannerBackend().updateFavorites(request.user, favorites)
        return redirect('/planner/')
