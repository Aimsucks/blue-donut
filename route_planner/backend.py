from eve_sde.models import SolarSystems, SolarSystemJumps
from jump_bridges.models import AnsiblexJumpGates
import networkx as nx


G = nx.Graph()

nodes = SolarSystems.objects.values_list('solarSystemID', flat=True)
edges = SolarSystemJumps.objects.values_list(
    'fromSolarSystemID', 'toSolarSystemID')
bridges = AnsiblexJumpGates.objects.values_list(
    'fromSolarSystemID', 'toSolarSystemID')

G.add_nodes_from(nodes)
G.add_edges_from(edges, type="gate")
G.add_edges_from(bridges, type="bridge")


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

        nodes = SolarSystems.objects.values_list('solarSystemID', flat=True)
        edges = SolarSystemJumps.objects.values_list(
            'fromSolarSystemID', 'toSolarSystemID')
        bridges = AnsiblexJumpGates.objects.values_list(
            'fromSolarSystemID', 'toSolarSystemID')

        G.add_nodes_from(nodes)
        G.add_edges_from(edges, type="gate")
        G.add_edges_from(bridges, type="bridge")
