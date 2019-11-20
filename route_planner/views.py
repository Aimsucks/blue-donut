from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from eve_esi import ESI
from eve_auth.models import EveUser
from route_planner.forms import DestinationForm, DestinationButton

from route_planner.backend import RoutePlannerBackend


class PlannerView(LoginRequiredMixin, View):
    def get(self, request):
        form = DestinationForm()
        button = DestinationButton()

        return render(
            request,
            'route_planner/planner.html',
            {
                'form': form,
            }
        )

    def post(self, request):
        form = DestinationForm(request.POST)
        button = DestinationButton(request.POST)

        if form.is_valid():
            try:
                character = request.user.characters.get(character_id=int(
                    request.POST['character_id']
                ))
            except EveUser.DoesNotExist:
                return HttpResponse(status=403)

            # req = ESI.request(
            #     'get_characters_character_id_location',
            #     client=character.get_client(),
            #     character_id=int(request.POST['character_id'])
            # )

            # source = req.data.solar_system_id
            # destination = form.data['destinationSystem']

            route = RoutePlannerBackend().generate(
                character,
                request.POST['character_id'],
                form.data['destinationSystem']
                )

            if 'verify' in request.POST:
                return render(
                    request,
                    'route_planner/planner.html',
                    {
                        'form': form,
                        'button': button,
                        'dotlan': route['dotlan'],
                        'destination': form.data['destinationSystem'],
                        'jumps': route['length'],
                        'mapDisplay': True,
                        'confirmButton': True,
                    }
                )
                print('verify')
            elif 'confirm' in request.POST:
                # for i in range(len(route)):
                #     if i == 0:
                #         ESI.request(
                #             'post_ui_autopilot_waypoint',
                #             client=character.get_client(),
                #             add_to_beginning=False,
                #             clear_other_waypoints=True,
                #             destination_id=route[i]
                #         )
                #     else:
                #         ESI.request(
                #             'post_ui_autopilot_waypoint',
                #             client=character.get_client(),
                #             add_to_beginning=False,
                #             clear_other_waypoints=False,
                #             destination_id=route[i]
                #         )
                print('confirm')
                return render(
                    request,
                    'route_planner/planner.html',
                    {
                        'form': form,
                        'dotlan': route['dotlan'],
                        'destination': form.data['destinationSystem'],
                        'jumps': route['length'],
                        'mapDisplay': True,
                        'confirmButton': False,
                    }
                )
            elif 'generate' in request.POST:
                # for i in range(len(route)):
                #     if i == 0:
                #         ESI.request(
                #             'post_ui_autopilot_waypoint',
                #             client=character.get_client(),
                #             add_to_beginning=False,
                #             clear_other_waypoints=True,
                #             destination_id=route[i]
                #         )
                #     else:
                #         ESI.request(
                #             'post_ui_autopilot_waypoint',
                #             client=character.get_client(),
                #             add_to_beginning=False,
                #             clear_other_waypoints=False,
                #             destination_id=route[i]
                #         )
                print('generate')
                return render(
                    request,
                    'route_planner/planner.html',
                    {
                        'form': form,
                        'dotlan': route['dotlan'],
                        'destination': form.data['destinationSystem'],
                        'jumps': route['length'],
                        'mapDisplay': True,
                        'confirmButton': False,
                    }
                )
            else:
                # for i in range(len(route)):
                #     if i == 0:
                #         ESI.request(
                #             'post_ui_autopilot_waypoint',
                #             client=character.get_client(),
                #             add_to_beginning=False,
                #             clear_other_waypoints=True,
                #             destination_id=route[i]
                #         )
                #     else:
                #         ESI.request(
                #             'post_ui_autopilot_waypoint',
                #             client=character.get_client(),
                #             add_to_beginning=False,
                #             clear_other_waypoints=False,
                #             destination_id=route[i]
                #         )
                print('quick')
                return render(
                    request,
                    'route_planner/planner.html',
                    {
                        'form': form,
                        'jumps': route['length'],
                        'mapDisplay': False,
                        'confirmButton': False,
                    }
                )
