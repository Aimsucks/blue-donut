from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from eve_esi import ESI
from eve_auth.models import EveUser

from route_planner.backend import RoutePlannerBackend

from dhooks import Webhook, Embed
hook = Webhook(settings.WEBHOOK_URL)


class PlannerView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'route_planner/planner.html')

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

        route = RoutePlannerBackend().generate(
            req,
            request.POST['destination']
        )

        if 'verify' in request.POST:
            return render(
                request,
                'route_planner/planner.html',
                {
                    'dotlan': route['dotlan'],
                    'destination': request.POST['destination'],
                    'jumps': route['length'],
                    'mapDisplay': True,
                    'confirmButton': True,
                }
            )
        elif 'confirm' in request.POST:
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
                    'dotlan': route['dotlan'],
                    'destination': request.POST['destination'],
                    'jumps': route['length'],
                    'mapDisplay': True,
                    'confirmButton': False,
                }
            )
        elif 'generate' in request.POST:
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
                    'dotlan': route['dotlan'],
                    'destination': request.POST['destination'],
                    'jumps': route['length'],
                    'mapDisplay': True,
                    'confirmButton': False,
                }
            )
        else:
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
                    'jumps': route['length'],
                    'mapDisplay': False,
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

        embed = Embed(
            description='An Ansiblex Jump Gate outage has been reported.',
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

        hook.send(embed=embed)

        return redirect('/planner/')


class SystemView(LoginRequiredMixin, View):
    def get(self, request, system):
        return render(request, 'route_planner/system.html', {'system': system})

