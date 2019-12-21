from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from eve_esi import ESI
from eve_auth.models import EveUser

from route_planner.backend import RoutePlannerBackend
from eve_sde.models import SolarSystems

from dhooks import Webhook, Embed
hook = Webhook(settings.WEBHOOK_URL)


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

        if source_name[0] == "J":
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
                    'message': "You cannot generate a route from a wormhole."
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


class ReportView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'route_planner/report.html')

    def post(self, request):
        try:
            character = request.user.characters.get(character_id=int(
                request.POST['characterID']
            ))
        except EveUser.DoesNotExist:
            return HttpResponse(status=403)

        reportSubmitter = ESI.request(
            'get_characters_character_id',
            client=character.get_client(),
            character_id=int(request.POST['characterID'])
        ).data.name

        outageType = request.POST['outageType']

        if outageType == "offline":
            embedDescription = "A jump gate is offline. Please contact the " \
                "owner to rectify the situation."
        elif outageType == "fuel":
            embedDescription = "A jump gate is out of fuel. Please contact " \
                "the owner to rectify the situation."
        elif outageType == "incorrect":
            embedDescription = "A pair of jump gates is correct. Use " \
                "addional information or check ingame to verify the report " \
                "is correct and fix the error."
        elif outageType == "loopback":
            embedDescription = "A jump gate has been moved but remains " \
                "in the same system. Please update the structure ID."
        elif outageType == "missing":
            embedDescription = "A jump gate is missing. Check ingame " \
                "and with logistics teams to see where it disappeared to."
        else:
            embedDescription = "There was a script error parsing the outage " \
                "type."

        embed = Embed(
            description=embedDescription,
            color=0x375A7F,
            timestamp='now'
        )

        reportSubmitterIcon = "https://image.eveonline.com/Character/" + \
            request.POST['characterID'] + "_32.jpg"
        footerIcon = "https://bluedonut.space/static/img/favicon.png"

        embed.set_author(name=reportSubmitter, icon_url=reportSubmitterIcon)
        embed.add_field(name="From System", value=request.POST['fromSystem'])
        embed.add_field(name="To System", value=request.POST['toSystem'])
        embed.set_footer(text="Blue Donut", icon_url=footerIcon)

        if (request.POST['structureID']):
            embed.add_field(name="Structure ID",
                            value=request.POST['structureID'],
                            inline=False)

        if (request.POST['extraInformation']):
            embed.add_field(name="Extra Information",
                            value=request.POST['extraInformation'],
                            inline=False)

        hook.send(embed=embed)

        return redirect('/planner/')


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
