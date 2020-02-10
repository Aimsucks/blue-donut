import random
from esi import ESI
from auth.models import EVEUser

search_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
search_string = " » "


class BridgesBackend:
    def search_routine(self, alliances):
        for alliance in alliances:
            self.get_character(alliance)

        return

    def get_character(self, alliance):
        characters = EVEUser.objects.filter(
            alliance_id=alliance,
            scope_search_structures=True,
            scope_read_structures=True
        )

        if not characters:
            return

        while True:
            character = random.choice(characters)
            try:
                alliance_esi = ESI.request(
                    'get_characters_character_id',
                    character_id=character.character_id
                ).data.alliance_id
            except KeyError:
                alliance_esi = 0

            if alliance == alliance_esi:
                break
            else:
                character.alliance_id = alliance_esi
                character.save()
                characters = characters.exclude(id__in=exclude_list)

            if not characters:
                break

        return character

    def structure_search(self, character, known_structures):
        return

    def structure_parse(self, character, structures):
        return

    def check_anomalies(self, structures):
        return

    def single_search(self, character, query):
        return
