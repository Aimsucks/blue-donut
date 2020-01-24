import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from eve_esi import ESI
from eve_auth.models import EveUser

from route_planner.backend import RoutePlannerBackend
from eve_sde.models import SolarSystems


class PlannerView(LoginRequiredMixin, View):
    def get(self, request):
        recents = RoutePlannerBackend().getInfo(request.user, 'recents')
        favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
        return render(request, 'route_planner/planner.html',
                      {'recents': recents,
                       'favorites': favorites})

    def post(self, request):
        try:
            character = request.user.characters.get(character_id=int(
                request.POST['character_id']
            ))
        except EveUser.DoesNotExist:
            return HttpResponse(status=403)

        req = ESI.request(
            'get_characters_character_id_location',
            client=character.get_client(),
            character_id=int(request.POST['character_id'])
        ).data.solar_system_id

        source_name = SolarSystems.objects.values_list(
            'solarSystemName', flat=True).get(solarSystemID=req)

        if re.match(r'J[0-9]{6}', source_name) or source_name == "Thera":
            recents = RoutePlannerBackend().getInfo(request.user, 'recents')
            favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
            return render(
                request,
                'route_planner/error.html',
                {
                    'recents': recents,
                    'favorites': favorites,
                    'mapDisplay': False,
                    'system': source_name,
                    'message': "You cannot generate a route from a wormhole. Try forcing a session change."
                }
            )

        route = RoutePlannerBackend().generate(
            req,
            request.POST['destination']
        )

        if 'verify' in request.POST:
            recents = RoutePlannerBackend().getInfo(request.user, 'recents')
            favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
            return render(
                request,
                'route_planner/planner.html',
                {
                    'recents': recents,
                    'favorites': favorites,
                    'dotlan': route['dotlan'],
                    'destination': request.POST['destination'],
                    'jumps': route['length'],
                    'mapDisplay': True,
                    'confirmButton': True,
                }
            )
        elif 'confirm' in request.POST:
            RoutePlannerBackend().updateRecents(
                request.user, request.POST['destination'])
            recents = RoutePlannerBackend().getInfo(request.user, 'recents')
            favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
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
            return render(
                request,
                'route_planner/planner.html',
                {
                    'recents': recents,
                    'favorites': favorites,
                    'dotlan': route['dotlan'],
                    'destination': request.POST['destination'],
                    'jumps': route['length'],
                    'mapDisplay': True,
                    'confirmButton': False,
                }
            )
        elif 'generate' in request.POST:
            RoutePlannerBackend().updateRecents(
                request.user, request.POST['destination'])
            recents = RoutePlannerBackend().getInfo(request.user, 'recents')
            favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
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
            return render(
                request,
                'route_planner/planner.html',
                {
                    'recents': recents,
                    'favorites': favorites,
                    'dotlan': route['dotlan'],
                    'destination': request.POST['destination'],
                    'jumps': route['length'],
                    'mapDisplay': True,
                    'confirmButton': False,
                }
            )
        else:
            RoutePlannerBackend().updateRecents(
                request.user, request.POST['destination'])
            recents = RoutePlannerBackend().getInfo(request.user, 'recents')
            favorites = RoutePlannerBackend().getInfo(request.user, 'favorites')
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
            return render(
                request,
                'route_planner/planner.html',
                {
                    'recents': recents,
                    'favorites': favorites,
                    'dotlan': route['dotlan'],
                    'destination': request.POST['destination'],
                    'jumps': route['length'],
                    'mapDisplay': True,
                    'confirmButton': False,
                }
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
