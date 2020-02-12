from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from map.models import System


class SystemsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        systems = System.objects.filter(id__lt=31000000).values_list('name', flat=True).order_by('name')
        return Response(systems)
