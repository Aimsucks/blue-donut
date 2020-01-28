from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from jump_bridges.backend import JumpBridgesBackend

from django.contrib.auth.models import User
from eve_auth.models import EveUser
from jump_bridges.models import AnsiblexJumpGates


class AccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ManagerView(AccessMixin, View):
    def get(self, request):
        data = {
            "accounts": User.objects.all().count(),
            "characters": EveUser.objects.all().count(),
            "scopes": EveUser.objects.filter(scope_search_structures=1).count(),
            "gates": AnsiblexJumpGates.objects.all().count(),
            "connections": int(AnsiblexJumpGates.objects.all().count()/2)
        }

        return render(request, 'jump_bridges/manager.html', {"data": data})

    def post(self, request):
        if 'update_gates' in request.POST:
            alliances = [
                498125261, 99003214, 99003838, 99001099, 99002367,
                99004116, 99001657, 99007289, 99008809, 99009104,
                99008469, 99005518, 741557221, 1411711376, 99002826
            ]

            gates = JumpBridgesBackend().search_routine(alliances)
            return render(request, 'jump_bridges/updated.html', {'number': gates, 'noun': 'gates'})

        elif 'update_characters' in request.POST:
            characters = JumpBridgesBackend().update_characters()
            return render(request, 'jump_bridges/updated.html', {'number': characters, 'noun': 'characters'})
