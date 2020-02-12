from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .backend import BridgesBackend


class UpdateBridges(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        alliances = [
            498125261
        ]
        number = BridgesBackend().search_routine(alliances)
        return Response(f'Updated {number} bridges.')
