from django.contrib.auth.models import User

from eve_auth.models import EveUser

SCOPE_NAMES = {
    'read_location': 'esi-location.read_location.v1',
    'write_waypoint': 'esi-ui.write_waypoint.v1',
    'search_structures': 'esi-search.search_structures.v1',
    'read_structures': 'esi-universe.read_structures.v1'
}

class EveAuthBackend:
    def authenticate(self, request, info=None, tokens=None):
        print(info)

        character_id = info['sub'].replace('CHARACTER:EVE:', '')
        name = info['name']
        scopes = info['scp']
        
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
        character.scope_read_location = SCOPE_NAMES['read_location'] in scopes
        character.scope_write_waypoint = SCOPE_NAMES['write_waypoint'] in scopes
        character.scope_search_structures = SCOPE_NAMES['search_structures'] in scopes
        character.scope_read_structures = SCOPE_NAMES['read_structures'] in scopes
        character.tokens = tokens

        character.save()

        return character.owner

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except EveUser.DoesNotExist:
            return None
