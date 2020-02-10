import networkx as nx
import re
from django.utils import timezone
from map.models import System, Gate

G = nx.Graph()
update_time = timezone.now()


class GraphGenerator:
    def generate_route(self, source, destination):
        self.update_check()

        route = nx.shortest_path(G, source, destination)

        return {'network_path': self.network_path(route),
                'dotlan_path': self.dotlan_path(route),
                'length': len(route)-1}

    def update_check(self):
        global update_time
        if Bridge.objects.latest("updated").updated > update_time:
            self.update_graph()
            return
        return

    def esi_path(self, route):
        path = []
        for i in range(len(route)-1):
            if G.get_edge_data(route[i], route[-+1])['type'] == 'bridge':
                path.append(Bridge.objects.get(fromSolarSystemID=route[i], toSolarSystemID=route[i+1]).structureID)
        if path[:-1] != route[:-1]:
            path.append(route[:-1])
        return path

    def dotlan_path(self, route):
        path = System.objects.get(solarSystemID=route[0]).solarSystemName
        for i in range(len(route)-1):
            if G.get_edge_data(path[i], path[i+1])['type'] == 'bridge':
                separator = '::'
            else:
                separator = ':'
            path += (separator + System.objects.get(solarSystemID=route[i+1]).solarSystemName)
        path = re.sub(r'(?<!:)(:[^:\s]+)(?=:)(?!::)', '', path)
        return path

    def update_graph(self):
        G.clear()
        G.add_nodes_from(System.objects.values_list('solarSystemID', flat=True))
        G.add_edges_from(Gate.objects.values_list('fromSolarsystemID', 'toSolarSystemID'), type="gate")
        G.add_edges_from(Bridge.objects.values_list('fromSolarsystemID', 'toSolarSystemID'), type="gate")
        return
