from django.contrib.auth.models import User
from django.utils import timezone
from auth.models import EVEUser

from esi import ESI

SCOPE_NAMES = {
    'read_location': 'esi-location.read_location.v1',
    'write_waypoint': 'esi-ui.write_waypoint.v1',
    'search_structures': 'esi-search.search_structures.v1',
    'read_structures': 'esi-universe.read_structures.v1'
}

class EVEAuthBackend:
    def authenticate(self, request, info=None, tokens=None):
        character_id = info['sub'].replace('CHARACTER:EVE:', '')
        name = info['name']
        scopes = info['scp']

        try:
            character = EVEUser.objects.get(character_id=character_id)
        except EVEUser.DoesNotExist:
            character = EVEUser(character_id=character_id)

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

        esi_data = ESI.request(
            'get_characters_character_id',
            character_id=character_id
        ).data

        try:
            character.alliance_id = esi_data.alliance_id
        except KeyError:
            character.alliance_id = 0
        character.corporation_id = esi_data.corporation_id

        # character.owner.characters.all().update(active=False)
        # character.active = True

        character.save()

        return character.owner

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except EVEUser.DoesNotExist:
            return None

    def check_alliance(self, character):
        if timezone.now() - character.esi_updated > timezone.timedelta(days=7):
            # logger.debug(f"Updating {character.name}'s alliance and corporation.")

            req = ESI.request(
                'get_characters_character_id',
                character_id=character.character_id
            ).data

            character.alliance_id = req.alliance_id
            character.corporation_id = req.corporation_id

            character.save()
            return
        return
