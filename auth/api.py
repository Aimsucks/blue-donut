from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from .serializers import CharacterSerializer


class CharacterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return self.request.user.characters.all()

    def patch(self, request):
        character = request.user.characters.get(character_id=request.data)

        if character:
            request.user.characters.all().update(active=False)
            print(character)
            character.active = True
            character.save()
            return request.user.characters.all()

        return Response(status=400, data="Wrong parameters.")
