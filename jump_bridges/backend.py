from eve_auth.models import EveUser
from jump_bridges.models import AnsiblexJumpGates
from eve_sde.models import SolarSystems
from eve_esi import ESI
import random

import logging
logger = logging.getLogger(__name__)

search_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
search_string = " » "

"""
Concerns:

How do we log everyone out so they have to re-authenticate with new scopes?
 - Drop all sessions and force everyone to log in again. (delete session table)

How do we automatically populate alliance and corporation IDs?

Need to check for single sided gates! (I think..)
"""

class JumpBridgesBackend:
    def search_routine(self, alliances):
        print("Beginning jump gate search routine.")

        missing_alliances = []
        excluded_gates = []
        jump_gates = []

        for alliance in alliances:
            characters = EveUser.objects.filter(alliance_id=alliance,
                                                scope_search_structures=True,
                                                scope_read_structures=True)

            # Check if there is a character in the desired alliance. If not, skip this iteration.
            if len(characters) == 0:
                print("No members found in alliance {}."
                      .format(alliance))
                missing_alliances.append(alliance)
                continue
            else:
                print("Found {} character(s) in {}."
                      .format(len(characters), alliance))

            # Verify this person is in the correct alliance.
            exclude_list = []

            while True:
                character = random.choice(characters)
                print("Checking if character {} is in alliance {}."
                      .format(character.name, alliance))

                try:
                    alliance_esi = ESI.request(
                        'get_characters_character_id',
                        character_id=character.character_id
                    ).data.alliance_id
                except KeyError:
                    alliance_esi = 0

                if alliance == alliance_esi:
                    print("Character {} is verified as a member of alliance {}."
                          .format(character.name, alliance))
                    break
                else:
                    print("Character's alliance has changed. Updating to {}."
                          .format(alliance_esi))
                    character.alliance_id = alliance_esi
                    character.save()

                    # Add the faulty character to the exclude list to avoid getting them again.
                    exclude_list.append(character.id)
                    characters = characters.exclude(id__in=exclude_list)

                if not characters:
                    break

            if not characters:
                print("Character list has been exhausted. Skipping alliance {}."
                      .format(alliance))
                continue

            character = EveUser.objects.get(character_id=character.character_id)

            new_gate_ids, new_gate_info = self.structure_search(character, excluded_gates)

            # Add results from the structure search to ignored gates for future searches
            excluded_gates.extend(new_gate_ids)

            jump_gates.extend(new_gate_info)

            # For loop is over - iterate to next alliance after adding the gates to the two lists

        print("Removing single sided gates.")
        final_list = self.check_single_gates(jump_gates)
        print("{} gates removed.".format(len(jump_gates)-len(final_list)))

        print("Updating database with {} total jump gates."
              .format(len(final_list)))

        # Clear the database and all all the gates to it
        AnsiblexJumpGates.objects.all().delete()

        for gate in final_list:
            fromSolarSystemID = SolarSystems.objects.get(solarSystemName=gate['from']).solarSystemID
            toSolarSystemID = SolarSystems.objects.get(solarSystemName=gate['to']).solarSystemID

            AnsiblexJumpGates(
                structureID=gate['id'],
                fromSolarSystemID=fromSolarSystemID,
                toSolarSystemID=toSolarSystemID,
                ownerID=gate['owner']
            ).save()

        print("Completed jump gate update routine.")
        print("Jump gates found: {}"
              .format(len(final_list)))
        if missing_alliances:
            print("Could not find members in the following alliances: {}"
                  .format(missing_alliances))

        return len(jump_gates)

    def structure_search(self, character, known_structures):
        print("Beginning deep search with character {}."
              .format(character.name))

        structure_ids = []

        # Search /characters/{character_id}/search/ for the "»" character and some letters
        # and add everything to a list
        for item in search_list:
            structure_ids.extend(ESI.request(
                'get_characters_character_id_search',
                client=character.get_client(),
                character_id=character.character_id,
                categories=['structure'],
                search=search_string+item
            ).data.structure)

            # Log the length of the structure list after every iteration

        print("List complete with {} structure IDs. Removing duplicates."
              .format(len(structure_ids)))

        structure_ids = list(dict.fromkeys(structure_ids))
        print("Duplicates removed. New total: {}"
              .format(len(structure_ids)))

        # Remove any structures we've already found
        structure_list = [x for x in structure_ids if x not in known_structures]

        print("Total structures to index: {}"
              .format(len(structure_list)))

        # Get information about each structure
        structure_info = self.structure_parse(character, structure_list)

        return structure_list, structure_info

    def single_search(self, character, query):
        try:
            gate_id = ESI.request(
                'get_characters_character_id_search',
                client=character.get_client(),
                character_id=character.character_id,
                categories=['structure'],
                search=query
            ).data.structure
        except KeyError:
            return

        # Note that searching for 2 systems and the "»" character will return two gates
        return self.structure_parse(character, gate_id)

    def structure_parse(self, character, structure_list):
        structure_info = []

        # Now query /universe/structures/{structure_id}/ to get information about each gate
        for item in structure_list:

            """
            Thinking about making it
                for index, item in enumerate(structure_list):
            so I can print the index every 10 or so times to gauge how fast it's going

            This would only be for when I get websockets working and can stream console
            output to the manager page to make sure functions are running correctly
            """

            req = ESI.request(
                'get_universe_structures_structure_id',
                client=character.get_client(),
                structure_id=item
            ).data

            name = req.name.split(' ')

            structure = {
                'id': item,
                'from': name[0],
                'to': name[2],
                'owner': req.owner_id
            }

            structure_info.append(structure.copy())

        return structure_info

    def check_single_gates(self, jump_gates):
        bad_list = []
        for gate in jump_gates:

            # Gates in "to" but not "from"
            if not gate["from"] in [d['to'] for d in jump_gates]:
                bad_list.append(gate["id"])

            # Gates in "from" but not "to"
            if not gate["to"] in [d['from'] for d in jump_gates]:
                bad_list.append(gate["id"])

        # Remove duplicates
        bad_list = list(dict.fromkeys(bad_list))

        # New list with all the single sided gates removed
        jump_gates = [item for item in jump_gates if item['id'] not in bad_list]

        return jump_gates

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

        return len(EveUser.objects.all())
        print("Character information updated!")
