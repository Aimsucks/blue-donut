from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.shortcuts import redirect

from uuid import uuid4

from esi import ESI

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Login(View):
    def get(self, request):
        scopes = [
            'esi-location.read_location.v1',
            'esi-ui.write_waypoint.v1',
            'esi-search.search_structures.v1',
            'esi-universe.read_structures.v1',
        ]
        return redirect(ESI.get_security().get_auth_uri(state=str(uuid4()), scopes=scopes))

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

class Callback(View):
    def get(self, request):
        security = ESI.get_security()

        tokens = security.auth(request.GET['code'])
        data = security.verify()

        login(request, authenticate(request, info=data, tokens=tokens))

        return redirect('/')

class Check(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = []

    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({})

        characters = []
        for character in request.user.characters.all():
            data = {
                'id': character.character_id,
                'name': character.name,
                'active': character.active
            }

            characters.append(data)

        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
            'characters': characters
        }

        return Response(content)
