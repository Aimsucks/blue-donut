from esi import ESI
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from auth.models import EVEUser
from bridges.models import Bridge
from map.models import System
import random
import re

from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)

search_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
search_string = " » "


class BridgesBackend:
    def manual_update(self, data):
        items = re.findall(r"(\d{13})\s([a-zA-Z0-9-]{6})\s-->\s([a-zA-Z0-9-]{6})", data)
        bridges = [{"id": int(x[0]), "from": x[1], "to": x[2]} for x in items]
        new_bridges = []
        for bridge in bridges:
            try:
                from_system = System.objects.get(name=bridge["from"])
            except ObjectDoesNotExist:
                return Response(status=400, data=f'System {bridge["from"]} does not exist')

            try:
                to_system = System.objects.get(name=bridge["to"])
            except ObjectDoesNotExist:
                return Response(status=400, data=f'System {bridge["to"]} does not exist')

            new_bridges.append({
                "id": bridge["id"],
                "from": from_system,
                "to": to_system,
            })

        new_bridges = self.check_anomalies(new_bridges)

        Bridge.objects.all().delete()
        with transaction.atomic():
            print(f'Beginning to add {len(new_bridges)} bridges to database...')
            for index, bridge in enumerate(new_bridges):
                Bridge(
                    id=bridge['id'],
                    from_system=bridge['from'],
                    to_system=bridge['to'],
                ).save()
                print(
                    f'    Progress: {index} out of approximately {len(new_bridges)}\r',
                    end=''
                )
            print(f'\nFinished adding {len(new_bridges)} bridges.')

        return Response(status=200, data=f'Added {len(new_bridges)} bridges')

    def search_routine(self, alliances):
        known_bridges = []
        bridges = []

        # Loop through each alliance
        for alliance in alliances:

            # Get a character object that has scopes
            character = self.get_character(alliance)

            # If you get none, move to a new alliance
            if not character:
                continue

            # Begin a search for bridges and add results to our lists
            new_bridge_ids, new_bridge_info = self.bridge_search(character, known_bridges)
            print(f'Discovered {len(new_bridge_ids)} new bridges.')
            known_bridges.extend(new_bridge_ids)
            bridges.extend(new_bridge_info)

        # The foor loop is over now, check for single sided bridges
        print(f'Checking {len(bridges)} bridges for anomalies.')
        bridges = self.check_anomalies(bridges)
        print(f'Found {len(bridges)} unique bridges.')

        # Begin modifying database
        if bridges:
            Bridge.objects.all().delete()
            with transaction.atomic():
                print(f'Beginning to add {len(bridges)} bridges to database...')
                for index, bridge in enumerate(bridges):
                    Bridge(
                        id=bridge['id'],
                        from_system=System.objects.get(name=bridge['from']),
                        to_system=System.objects.get(name=bridge['to']),
                        owner_id=bridge['owner']
                    ).save()
                    print(
                        f'    Progress: {index} out of approximately {len(bridges)}\r',
                        end=''
                    )
                print(f'\nFinished adding {len(bridges)} bridges.')

        return len(bridges)

    # Get a character from the specified alliance with the correct scopes
    def get_character(self, alliance):

        # Get a list of characters in that alliance with proper scopes
        characters = EVEUser.objects.filter(
            alliance_id=alliance,
            scope_search_structures=True,
            scope_read_structures=True
        )

        if not characters:
            return

        # List of characters that are not in our alliance (but the db thinks they are)
        exclude_list = []

        # Loop through characters until one in the alliance we want is found
        while characters:
            character = random.choice(characters)
            try:
                alliance_esi = ESI.request(
                    'get_characters_character_id',
                    character_id=character.character_id
                ).data.alliance_id
            except KeyError:
                alliance_esi = 0

            # This is our verification condition
            if alliance == alliance_esi:
                break

            # If inaccurate, update the charcter and add them to the exclude list
            else:
                character.alliance_id = alliance_esi
                character.save()

                exclude_list.append(character.id)
                characters = characters.exclude(id__in=exclude_list)

        # If the loop finishes and we get nothing, return to main function
        if not characters:
            return

        return character

    # Use /characters/{character_id}/search/ to find a list of bridge IDs
    def bridge_search(self, character, known_bridges):
        bridge_ids = []

        print(f'Beginning to search with {len(search_list)} unique strings.')

        # Loop through the alphanumeric list at the top of the file
        # Searches for " » A", " » B", and so on
        for index, item in enumerate(search_list):

            # Append the results to our list
            bridge_ids.extend(
                ESI.request(
                    'get_characters_character_id_search',
                    client=character.get_client(),
                    character_id=character.character_id,
                    categories=['structure'],
                    search=search_string+item
                ).data.structure
            )
            print(
                f'    Progress: {index} out of approximately {len(search_list)}\r',
                end=''
            )
        print(f'\nFinished searching {len(search_list)} times.')

        # Remove duplicates
        bridge_ids = list(set(bridge_ids))

        # Remove bridges that are in known_bridges (to prevent excess API queries)
        bridge_list = [x for x in bridge_ids if x not in known_bridges]

        bridge_info = self.bridge_parse(character, bridge_list)

        return bridge_list, bridge_info

    # Parse information from /universe/structures/{structure_id}/
    def bridge_parse(self, character, bridge_list):
        bridge_info = []

        print(f'Beginning to parse {len(bridge_list)} bridges.')

        # Loop through bridge IDs
        # The bridge search only returns structures the character can parse
        for index, item in enumerate(bridge_list):
            req = ESI.request(
                'get_universe_structures_structure_id',
                client=character.get_client(),
                structure_id=item
            ).data
            name = req.name.split(' ')

            bridge = {
                'id': item,
                'from': name[0],
                'to': name[2],
                'owner': req.owner_id
            }
            bridge_info.append(bridge.copy())
            print(
                f'    Progress: {index} out of approximately {len(bridge_list)}\r',
                end=''
            )
        print(f'\nFinished parsing {len(bridge_list)} bridges.')

        return bridge_info

    # Checks for single sided bridges (no connection but show up still)
    def check_anomalies(self, bridges):
        bad_list = []
        for bridge in bridges:

            # Bridges in "to" but not "from"
            if not bridge["from"] in [d['to'] for d in bridges]:
                bad_list.append(bridge["id"])

            # Bridges in "from" but not "to"
            if not bridge['to'] in [d['from'] for d in bridges]:
                bad_list.append(bridge['id'])

        # Remove duplicates
        bad_list = list(set(bad_list))

        # New list with all the single sided bridges removed
        bridges = [item for item in bridges if item['id'] not in bad_list]

        return bridges

    # Search for a set of bridges (used in report form)
    def single_search(self, character, query):
        try:
            bridge_id = ESI.request(
                'get_characters_character_id_search',
                client=character.get_client(),
                character_id=character.character_id,
                categories=['structure'],
                search=query
            ).data.structure
        except KeyError:
            return

        # Note that searching for 2 systems and the "»" character will return two gates
        return self.bridge_parse(character, bridge_id)
