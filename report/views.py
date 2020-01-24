from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render, redirect
from report.backend import ReportBackend


class ReportView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'report/report.html'
        )

    def post(self, request):
        ReportBackend().send_webhook(request, ReportBackend().update_gate(request))
        return redirect('/planner/')
