import networkx as nx
import re

from eve_esi import ESI
from eve_sde.models import SolarSystems, SolarSystemJumps
from jump_bridges.models import AnsiblexJumpGates

import logging

logger = logging.getLogger(__name__)

G = nx.Graph()


class RoutePlannerBackend:
    def generate(self, character, character_id, system):

        req = ESI.request(
            'get_characters_character_id_location',
            client=character.get_client(),
            character_id=int(character_id)
        ).data
        source = req.solar_system_id
        source_name = req.solar_system_name

        destination = SolarSystems.objects.values_list(
            'solarSystemID', flat=True).get(solarSystemName=system)

        path = nx.shortest_path(G, source, destination)
        path_length = len(path)-1

        jb_path = []
        for i in range(len(path)-1):
            if G.get_edge_data(path[i], path[i+1])['type'] == 'bridge':
                jb_path.append(AnsiblexJumpGates.objects.values_list(
                    'structureID', flat=True).get(
                    fromSolarSystemID=path[i], toSolarSystemID=path[i+1]))
        if jb_path[:-1] != destination:
            jb_path.append(destination)

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
