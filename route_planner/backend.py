from eve_sde.models import SolarSystems, SolarSystemJumps
from jump_bridges.models import AnsiblexJumpGates
import networkx as nx

import logging

logger = logging.getLogger(__name__)

G = nx.Graph()
logger.debug("Graph created.")


class RoutePlannerBackend:
    def generate(self, source, destination):
        start = source
        finish = SolarSystems.objects.values_list(
            'solarSystemID', flat=True).get(solarSystemName=destination)

        path = nx.shortest_path(G, start, finish)

        jb_path = []

        for i in range(len(path)-1):
            if G.get_edge_data(path[i], path[i+1])['type'] == 'bridge':
                jb_path.append(AnsiblexJumpGates.objects.values_list(
                    'structureID', flat=True).get(
                    fromSolarSystemID=path[i], toSolarSystemID=path[i+1]))

        jb_path.append(finish)

        return jb_path

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
