from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render


class PlannerView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'route_planner/planner.html',
            {
                'user': request.user,
                'characters': request.user.characters
            }
        )
