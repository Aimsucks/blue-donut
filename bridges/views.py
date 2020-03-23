from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .backend import BridgesBackend


class AutoUpdateBridges(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        # alliances = [
        #     498125261
        # ]
        # number = BridgesBackend().search_routine(alliances)
        # return Response(f'Updated {number} bridges.')
        return Response(status=400, data="Feature is currently disabled")

class ManualUpdateBridges(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        response = BridgesBackend().manual_update(request.data["data"])
        return response
