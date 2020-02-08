from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from .serializers import CharacterSerializer


class CharacterViewSet(mixins.ListModelMixin,
                       #    mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.AllowAny]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    permission_classes = [permissions.AllowAny]
    serializer_class = CharacterSerializer
    queryset = ""

    def list(self, request):
        if request.user.is_anonymous:
            return Response(None)

        queryset = request.user.characters.all()
        serializer = CharacterSerializer(queryset, many=True)
        return Response(serializer.data)

    # def patch(self, request, pk=None):
    #     if request.user.is_anonymous:
    #         return Response(None)

    #     request.user.characters.all().update(active=False)

    #     character = request.user.characters.get(character_id=request.data["character_id"])
    #     character.active = True
    #     character.save()

    #     queryset = request.user.characters.all()
    #     serializer = CharacterSerializer(queryset, many=True)

    #     return Response(serializer.data)
