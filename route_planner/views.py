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
                        'form': form,
                        'dotlan': route['dotlan'],
                        'destination': form.data['destinationSystem'],
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
                        'form': form,
                        'dotlan': route['dotlan'],
                        'destination': form.data['destinationSystem'],
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
                        'form': form,
                        'jumps': route['length'],
                        'mapDisplay': False,
                        'confirmButton': False,
                    }
                )
