from django.contrib.auth.models import User

from eve_auth.models import EveUser


class EveAuthBackend:
    def authenticate(self, request, info=None, tokens=None):
        character_id = info['sub'].replace('CHARACTER:EVE:', '')
        name = info['name']
        try:
            character = EveUser.objects.get(character_id=character_id)
        except EveUser.DoesNotExist:
            character = EveUser(character_id=character_id)

        if request.user.is_authenticated:
            character.owner = request.user
        elif hasattr(character, 'owner'):
            pass
        elif User.objects.filter(username=name).exists():
            character.owner = User.objects.get(username=name)
        else:
            character.owner = User.objects.create_user(name)

        character.name = info['name']
        character.tokens = tokens

        character.save()

        return character.owner

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except EveUser.DoesNotExist:
            return None
