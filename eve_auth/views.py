from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.shortcuts import render, redirect

from uuid import uuid4

from eve_esi import ESI


class LoginView(View):
    def get(self, request):
        return render(request, "eve_auth/scope_selection.html")

    def post(self, request):
        scopes = [
            'esi-location.read_location.v1',
            'esi-ui.write_waypoint.v1',
        ]

        if "approve" in request.POST:
            scopes.extend([
                'esi-search.search_structures.v1',
                'esi-universe.read_structures.v1'
            ])

        return redirect(
            ESI.get_security().get_auth_uri(state=str(uuid4()), scopes=scopes)
        )

class CallbackView(View):
    def get(self, request):
        security = ESI.get_security()

        tokens = security.auth(request.GET['code'])
        data = security.verify()

        login(request, authenticate(request, info=data, tokens=tokens))

        return redirect('/')
