from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from jump_bridges.forms import JumpBridgeForm
from jump_bridges.models import AnsiblexJumpGates

from eve_sde.models import SolarSystems

from route_planner.backend import RoutePlannerBackend

from eve_esi import ESI

search_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
search_string = " » "

class AccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ManagerView(AccessMixin, View):

    def get(self, request):

        structure_list = []
        ansiblex_list = []

        character = request.user.characters.get(character_id=2113697818)

        for item in search_list:
            structure_list.extend(ESI.request(
                'get_characters_character_id_search',
                client=character.get_client(),
                character_id=2113697818,
                categories=['structure'],
                search=search_string+item
            ).data.structure)
            print(len(structure_list))

        print("---")

        structure_list = list(dict.fromkeys(structure_list))
        print(len(structure_list))

        print("---")

        for item in structure_list:
            req = ESI.request(
                'get_universe_structures_structure_id',
                client=character.get_client(),
                structure_id=item
            ).data.name.split(' ')

            formatted_string = str(item) + " " + req[0] + " --> " + req[2]
            print(formatted_string)

        print("Finished!")

        return render(request, 'jump_bridges/automatic.html')
        # form = JumpBridgeForm()

        # return render(
        #     request,
        #     'jump_bridges/manager.html',
        #     {
        #         'form': form
        #     }
        # )

    def post(self, request):
        # form = JumpBridgeForm(request.POST)

        # if form.is_valid():
        #     split = request.POST['jumpBridges'].split('\r\n')
        #     bridges = [item for item in split if '10' in item]

        #     AnsiblexJumpGates.objects.all().delete()

        #     for item in bridges:
        #         structureID = item[0:13]
        #         fromSolarSystemID = SolarSystems.objects.values_list(
        #             'solarSystemID', flat=True).get(
        #                 solarSystemName=item[14:20])
        #         toSolarSystemID = SolarSystems.objects.values_list(
        #             'solarSystemID', flat=True).get(
        #                 solarSystemName=item[25:31])
        #         AnsiblexJumpGates(
        #             structureID=structureID,
        #             fromSolarSystemID=fromSolarSystemID,
        #             toSolarSystemID=toSolarSystemID).save()

        #     RoutePlannerBackend().updateGraph()

        return redirect('/manager/')
