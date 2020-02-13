import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from auth.models import EVEUser
from auth.backend import EVEAuthBackend
from esi import ESI
from map.models import System
from planner.models import PopularSystems

from .backend import GraphGenerator, Lister


class GenerateRoute(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print(request.data)
        planner = GraphGenerator()

        # Making sure we have all the parameters we need
        if 'to' not in request.data or 'character' not in request.data:
            return Response(status=400)

        # Character ID check
        try:
            character = request.user.characters.get(character_id=int(request.data['character']))
        except EVEUser.DoesNotExist:
            return Response(status=400)

        # Double-check the character's alliance (mostly for updating it if it's wrong)
        EVEAuthBackend().check_alliance(character)

        # Making sure we're going to a real system
        try:
            to_system = System.objects.get(name=request.data['to']).id
        except System.DoesNotExist:
            return Response(status=400)

        # Handling if the user wants to specify a start point
        if request.data.get('from', False):
            try:
                from_system = System.objects.get(name=request.data['from']).id
            except System.DoesNotExist:
                return Response(status=400)
        else:
            from_system = ESI.request(
                'get_characters_character_id_location',
                client=character.get_client(),
                character_id=int(request.data['character'])
            ).data.solar_system_id

        # Wormhole system check
        if from_system > 31000000:
            return Response(status=400)

        if request.data.get('avoid', False):
            avoid_systems = request.data['avoid']
        else:
            avoid_systems = None

        route = planner.generate_route(from_system, to_system, avoid_systems)
        route['destination'] = request.data['to']
        route['confirm_button'] = True
        if 'confirm' in request.data:
            planner.send_route(character, route['network_path'])
            route['confirm_button'] = False
        return Response(route)


class Popular(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        try:
            popular = PopularSystems.objects.get(id=1).popular
        except PopularSystems.DoesNotExist or AttributeError:
            popular = PopularSystems(popular=json.dumps([None, None, None, None, None]))
            popular.save()
            popular = PopularSystems.objects.get(id=1).popular
        return Response(json.loads(popular))


class Favorites(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        favorites, recents = Lister().get_lists(request.user)
        return Response(favorites)

    def post(self, request, format=None):
        favorites = Lister().update_favorites(request.user, request.POST['favorites'])
        return Response(favorites)


class Recents(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        favorites, recents = Lister().get_lists(request.user)
        return Response(recents)
