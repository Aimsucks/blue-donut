import networkx as nx
import re
import json

from eve_sde.models import SolarSystems, SolarSystemJumps
from jump_bridges.models import AnsiblexJumpGates
from route_planner.models import PlannerLists

import logging

logger = logging.getLogger(__name__)

G = nx.Graph()


class RoutePlannerBackend:
    def generate(self, source_id, destination_name):
        source_name = SolarSystems.objects.values_list(
            'solarSystemName', flat=True).get(solarSystemID=source_id)

        destination_id = SolarSystems.objects.values_list(
            'solarSystemID', flat=True).get(solarSystemName=destination_name)

        print("----------")
        print("Source: " + source_name)
        print("Destination: " + destination_name)

        logger.debug("----------")
        logger.debug("Source: " + source_name)
        logger.debug("Destination: " + destination_name)

        path = nx.shortest_path(G, source_id, destination_id)
        path_length = len(path)-1

        jb_path = []
        for i in range(len(path)-1):
            if G.get_edge_data(path[i], path[i+1])['type'] == 'bridge':
                debug_first_system = SolarSystems.objects.values_list(
                    'solarSystemName', flat=True).get(solarSystemID=path[i])
                debug_second_system = SolarSystems.objects.values_list(
                    'solarSystemName', flat=True).get(solarSystemID=path[i+1])
                print(debug_first_system + " -> " + debug_second_system)
                logger.debug(debug_first_system + " -> " + debug_second_system)
                jb_path.append(AnsiblexJumpGates.objects.values_list(
                    'structureID', flat=True).get(
                    fromSolarSystemID=path[i], toSolarSystemID=path[i+1]))
        if jb_path[:-1] != destination_id:
            jb_path.append(destination_id)

        print("Route generated successfully!")
        logger.debug("Route generated successfully!")

        dotlan_path = source_name
        for i in range(len(path)-1):
            if G.get_edge_data(path[i], path[i+1])['type'] == 'bridge':
                bridged_path = '::' + SolarSystems.objects.values_list(
                    'solarSystemName', flat=True).get(solarSystemID=path[i+1])
                dotlan_path += bridged_path

            else:
                gated_path = ':' + SolarSystems.objects.values_list(
                    'solarSystemName', flat=True).get(solarSystemID=path[i+1])
                dotlan_path += gated_path
        dotlan_path = re.sub('(?<!:)(:[^:\s]+)(?=:)(?!::)', '', dotlan_path)

        result = {
            'esi': jb_path,
            'dotlan': dotlan_path,
            'length': path_length
        }

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
