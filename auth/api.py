from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import CharacterSerializer


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        if request.user.is_anonymous:
            return Response(False)
        return Response(True)


class CharacterViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = request.user.characters.all()
        serializer = CharacterSerializer(queryset, many=True)
        return Response(serializer.data)


"""
Add in ability to delete a specific character if the user owns it.
Also add a profile page where you can manage characters.
"""
