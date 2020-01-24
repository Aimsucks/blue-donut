from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from jump_bridges.backend import JumpBridgesBackend

class AccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ManagerView(AccessMixin, View):

    def get(self, request):
        return render(
            request,
            'jump_bridges/manager.html'
        )

    def post(self, request):
        alliances = [
            498125261,
            99003214,
            99003838,
            99001099,
            99002367,
            99004116,
            99001657,
            99007289,
            99008809,
            99009104,
            99008469,
            99005518,
            741557221,
            1411711376,
            99002826
        ]

        gates = JumpBridgesBackend().search_routine(alliances)

        return render(
            request,
            'jump_bridges/manager.html',
            {
                'gates_added': gates
            }
        )
