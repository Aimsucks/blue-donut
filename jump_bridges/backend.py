from eve_auth.models import EveUser
# from jump_bridges.models import AnsiblexJumpGates
from eve_esi import ESI
import random

import logging

logger = logging.getLogger(__name__)

search_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
search_string = " » "

"""
Concerns:

How do you get the master list of structure IDs so you dont duplicate already-found gates
    and only do newly discovered ones from a different character's search?

How do we log everyone out so they have to re-authenticate with new scopes?
"""

class JumpBridgesBackend:
    def search_routine(self, request, alliances):
        print("Beginning jump gate search routine.")

        for alliance in alliances:

            """
            Need a try + except here in case we don't have a character from a certain alliance!
            """
            members = EveUser.objects.filter(alliance_id=alliance)
            print("Found {} character(s) in {}.".format(len(members), alliance))

            member = random.choice(members)

            # Verify this person is in the correct alliance.
            alliance_esi = ESI.request(
                'get_characters_character_id',
                character_id=member.character_id
            ).data.alliance_id

            """
            Add something here to update the character's alliance if it isn't correct in the database.
            """

            while alliance_esi != alliance:
                member = random.choice(members)

                alliance_esi = ESI.request(
                    'get_characters_character_id',
                    character_id=member
                ).data.alliance_id

            print("Character {} is verified as a member of alliance {}.".format(member.name, alliance))

            character = request.user.characters.get(character_id=member.character_id)
            print(character)

            print(len(JumpBridgesBackend.deep_search(self, character)))

    def deep_search(self, character):
        print("Beginning deep search with character {}.".format(character.name))

        structure_ids = []

        # Search /characters/{character_id}/search/ for the ">>" character and some letters
        # and add everything to a list
        for item in search_list:
            structure_ids.extend(ESI.request(
                'get_characters_character_id_search',
                client=character.get_client(),
                character_id=2113697818,
                categories=['structure'],
                search=search_string+item
            ).data.structure)

            # Log the length of the structure list after every iteration
            print(len(structure_ids))

        print("---")

        # Remove all duplicates from the list
        structure_ids = list(dict.fromkeys(structure_ids))

        print(len(structure_ids))

        print("---")

        structure_list = []

        # Now query /universe/structures/{structure_id}/ to get information about each gate
        for item in structure_ids:
            req = ESI.request(
                'get_universe_structures_structure_id',
                client=character.get_client(),
                structure_id=item
            ).data

            name = req.name.split(' ')

            structure_list.extend({
                'id': item,
                'from': name[0],
                'to': name[2],
                'owner': req.owner_id
            })

        return structure_list

        """
        Still need to add code to update database or produce a list with the shit thats going in.
        """

    def update_characters(self):
        print("Updating character alliances and corporations.")

        for character in EveUser.objects.all():

            data = ESI.request(
                'get_characters_character_id',
                character_id=character.character_id
            ).data

            if "alliance_id" in data:
                alliance = data.alliance_id
            else:
                alliance = 0

            corporation = data.corporation_id

            character.alliance_id = alliance
            character.corporation_id = corporation

            character.save()

        print("Character information updated!")
