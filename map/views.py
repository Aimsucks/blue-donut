from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from map.models import System


class SystemsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        deadspace = [10000004, 10000019, 10000017]
        systems = System.objects.filter(id__lt=31000000).exclude(
            region__id__in=deadspace).values_list('name', flat=True).order_by('name')
        return Response(systems)
