from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from jump_bridges.forms import JumpBridgeForm
from jump_bridges.models import AnsiblexJumpGates

from eve_sde.models import SolarSystems

from route_planner.backend import RoutePlannerBackend

from jump_bridges.backend import JumpBridgesBackend

class AccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


"""
Need to figure out an interface for the automation tool.
"""

class ManagerView(AccessMixin, View):

    def get(self, request):
        JumpBridgesBackend().search_routine(request, [498125261])
        # JumpBridgesBackend.update_characters(self)
        # JumpBridgesBackend.test_function(self)

        return render(
            request,
            'jump_bridges/manager.html'
        )

    # def post(self, request):
    #     form = JumpBridgeForm(request.POST)

    #     if form.is_valid():
    #         split = request.POST['jumpBridges'].split('\r\n')
    #         bridges = [item for item in split if '10' in item]

    #         AnsiblexJumpGates.objects.all().delete()

    #         for item in bridges:
    #             structureID = item[0:13]
    #             fromSolarSystemID = SolarSystems.objects.values_list(
    #                 'solarSystemID', flat=True).get(
    #                     solarSystemName=item[14:20])
    #             toSolarSystemID = SolarSystems.objects.values_list(
    #                 'solarSystemID', flat=True).get(
    #                     solarSystemName=item[25:31])
    #             AnsiblexJumpGates(
    #                 structureID=structureID,
    #                 fromSolarSystemID=fromSolarSystemID,
    #                 toSolarSystemID=toSolarSystemID).save()

    #         RoutePlannerBackend().updateGraph()

    #     return redirect('/manager/')
