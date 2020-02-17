from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .backend import ReportBackend


class Report(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        backend = ReportBackend()
        status, text = backend.send_webhook(request)
        return Response(status=status, data=text)
