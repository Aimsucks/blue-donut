from eve_auth.models import EveUser
from jump_bridges.models import AnsiblexJumpGates
from eve_sde.models import SolarSystems
from eve_esi import ESI
import random

import logging
logger = logging.getLogger(__name__)

search_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
search_string = " » "

class JumpBridgesBackend:
    def search_routine(self, alliances):
        logger.debug("Beginning jump gate search routine.")

        missing_alliances = []
        excluded_gates = []
        jump_gates = []

        for alliance in alliances:
            characters = EveUser.objects.filter(alliance_id=alliance,
                                                scope_search_structures=True,
                                                scope_read_structures=True)

            # Check if there is a character in the desired alliance. If not, skip this iteration.
            if not characters:
                logger.debug(f"No members found in alliance {alliance}.")
                missing_alliances.append(alliance)
                continue
            else:
                logger.debug(f"Found {len(characters)} character(s) in {alliance}.")

            # Verify this person is in the correct alliance.
            exclude_list = []

            while True:
                character = random.choice(characters)
                logger.debug(f"Checking if character {character.name} is in alliance {alliance}.")

                try:
                    alliance_esi = ESI.request(
                        'get_characters_character_id',
                        character_id=character.character_id
                    ).data.alliance_id
                except KeyError:
                    alliance_esi = 0

                if alliance == alliance_esi:
                    logger.debug(f"Character {character.name} is verified as a member of alliance {alliance}.")
                    break
                else:
                    logger.debug(f"Character's alliance has changed. Updating to {alliance_esi}.")
                    character.alliance_id = alliance_esi
                    character.save()

                    # Add the faulty character to the exclude list to avoid getting them again.
                    exclude_list.append(character.id)
                    characters = characters.exclude(id__in=exclude_list)

                if not characters:
                    break

            if not characters:
                logger.debug(f"Character list has been exhausted. Skipping alliance {alliance}.")
                continue

            character = EveUser.objects.get(character_id=character.character_id)

            new_gate_ids, new_gate_info = self.structure_search(character, excluded_gates)

            # Add results from the structure search to ignored gates for future searches
            excluded_gates.extend(new_gate_ids)

            jump_gates.extend(new_gate_info)

            # For loop is over - iterate to next alliance after adding the gates to the two lists

        logger.debug("Removing single sided gates.")
        final_list = self.check_single_gates(jump_gates)

        logger.debug(f"{len(jump_gates)-len(final_list)} gates removed.")

        logger.debug(f"Updating database with {len(final_list)} total jump gates.")

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

        logger.debug("Completed jump gate update routine.")
        logger.debug(f"Jump gates found: {len(final_list)}")
        if missing_alliances:
            logger.debug(f"Could not find members in the following alliances: {missing_alliances}")

        return len(jump_gates)

    def structure_search(self, character, known_structures):
        logger.debug(f"Beginning deep search with character {character}.")

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

        logger.debug(f"List complete with {structure_ids} structure IDs. Removing duplicates.")

        structure_ids = list(set(structure_ids))
        logger.debug(f"Duplicates removed. New total: {structure_ids}")

        # Remove any structures we've already found
        structure_list = [x for x in structure_ids if x not in known_structures]

        logger.debug(f"Total structures to index: {structure_list}")

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
        bad_list = list(set(bad_list))

        # New list with all the single sided gates removed
        jump_gates = [item for item in jump_gates if item['id'] not in bad_list]

        return jump_gates

    def update_characters(self):
        logger.debug("Updating character alliances and corporations.")

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
        logger.debug("Character information updated!")
