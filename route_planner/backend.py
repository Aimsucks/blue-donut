import networkx as nx
import re
import json

from eve_sde.models import SolarSystems, SolarSystemJumps
from jump_bridges.models import AnsiblexJumpGates
from route_planner.models import PlannerLists
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

G = nx.Graph()
update_time = timezone.now()

class RoutePlannerBackend:
    def generate(self, source_id, destination_name):

        # Snippet to make sure graph is up to date
        global update_time
        database_time = AnsiblexJumpGates.objects.latest("updated").updated
        if database_time > update_time:
            logger.debug("Graph is out of date - updating.")
            update_time = timezone.now()
            self.updateGraph()

        source_name = SolarSystems.objects.get(solarSystemID=source_id).solarSystemName
        destination_id = SolarSystems.objects.get(solarSystemName=destination_name).solarSystemID

        logger.debug("----------")
        logger.debug(f"Source: {source_name}")
        logger.debug(f"Destination: {destination_name}")

        path = nx.shortest_path(G, source_id, destination_id)
        path_length = len(path)-1

        jb_path = []
        for i in range(len(path)-1):
            if G.get_edge_data(path[i], path[i+1])['type'] == 'bridge':
                debug_first_system = SolarSystems.objects.get(solarSystemID=path[i]).solarSystemName
                debug_second_system = SolarSystems.objects.get(solarSystemID=path[i+1]).solarSystemName

                print(debug_first_system + " -> " + debug_second_system)

                jb_path.append(AnsiblexJumpGates.objects.get(
                    fromSolarSystemID=path[i], toSolarSystemID=path[i+1]).structureID)

        if jb_path[:-1] != destination_id:
            jb_path.append(destination_id)

        logger.debug("Route generated successfully!")

        dotlan_path = source_name
        for i in range(len(path)-1):
            if G.get_edge_data(path[i], path[i+1])['type'] == 'bridge':
                bridged_path = '::' + SolarSystems.objects.get(solarSystemID=path[i+1]).solarSystemName
                dotlan_path += bridged_path
            else:
                gated_path = ':' + SolarSystems.objects.get(solarSystemID=path[i+1]).solarSystemName
                dotlan_path += gated_path
        dotlan_path = re.sub(r'(?<!:)(:[^:\s]+)(?=:)(?!::)', '', dotlan_path)

        result = {'esi': jb_path, 'dotlan': dotlan_path, 'length': path_length}

        return result

    def updateGraph(self):
        G.clear()
        logger.debug("Graph cleared.")

        nodes = SolarSystems.objects.values_list('solarSystemID', flat=True)
        edges = SolarSystemJumps.objects.values_list(
            'fromSolarSystemID', 'toSolarSystemID')
        bridges = AnsiblexJumpGates.objects.values_list(
            'fromSolarSystemID', 'toSolarSystemID')

        G.add_nodes_from(nodes)
        logger.debug("Graph nodes added.")
        G.add_edges_from(edges, type="gate")
        logger.debug("Standard gate edges added.")
        G.add_edges_from(bridges, type="bridge")
        logger.debug("Ansiblex gate edges added.")

    def getInfo(self, user, list_name):
        try:
            character = PlannerLists.objects.get(user_id=user)
        except PlannerLists.DoesNotExist:
            character = PlannerLists(user_id=user.id)
            character.recents = json.dumps([None] * 5)
            character.favorites = json.dumps([None] * 5)
            character.save()

        if list_name == 'favorites':
            return json.loads(character.favorites)
        if list_name == 'recents':
            return json.loads(character.recents)

    def updateRecents(self, user, system):
        character = PlannerLists.objects.get(user_id=user)
        recents = json.loads(character.recents)
        if system not in recents:
            recents.insert(0, system)
            recents.pop()
        else:
            recents.remove(system)
            recents.insert(0, system)
        character.recents = json.dumps(recents)
        character.save()

    def updateFavorites(self, user, favorites):
        for i in range(len(favorites)):
            if favorites[i] == '':
                favorites[i] = None
        character = PlannerLists.objects.get(user_id=user)
        character.favorites = json.dumps(favorites)
        character.save()
