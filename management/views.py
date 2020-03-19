from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from auth.models import EVEUser
from bridges.models import Bridge
from map.models import System


class Statistics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "users":
            [
                {
                    "name": "Users",
                    "number": User.objects.all().count()
                },
                {
                    "name": "Characters",
                    "number": EVEUser.objects.all().count()
                },
                {
                    "name": "Scopes",
                    "number": EVEUser.objects.filter(scope_search_structures=1).count()
                }
            ],
            "bridges":
            [
                {
                    "name": "Bridges",
                    "number": Bridge.objects.all().count()
                },
                {
                    "name": "Connections",
                    "number": int(Bridge.objects.all().count()/2)
                },
            ],
            "map":
            [
                {
                    "name": "Systems",
                    "number": System.objects.all().count()
                }
            ]
        }
        return Response(data)
