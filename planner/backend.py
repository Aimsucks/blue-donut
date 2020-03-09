import networkx as nx
import re
import json

from django.utils import timezone
from django.conf import settings
from django.db.utils import OperationalError

from esi import ESI
from map.models import System, Gate
from bridges.models import Bridge
from planner.models import PlannerLists

G = nx.Graph()
update_time = timezone.now()


class GraphGenerator:
    def generate_route(self, source, destination, avoid=None):
        self.update_check()

        if avoid:
            E = G.copy()
            for system in avoid:
                E.remove_node(System.objects.get(name=system).id)
            route = nx.shortest_path(E, source, destination)
        else:
            route = nx.shortest_path(G, source, destination)

        return {'network_path': self.network_path(route),
                'dotlan_path': self.dotlan_path(route),
                'length': len(route)-1}

    def update_check(self):
        global update_time
        try:
            if Bridge.objects.latest("updated").updated > update_time:
                self.update_graph()
                return
        except Bridge.DoesNotExist:
            return
        return

    def network_path(self, route):
        path = [route[0]]
        for i in range(len(route)-1):
            if G.get_edge_data(route[i], route[i+1])['type'] == 'bridge':
                path.append(Bridge.objects.get(from_system__id=route[i], to_system__id=route[i+1]).id)

        if (len(path) == 0) or (path[-1] != route[-1]):
            path.append(route[-1])
        return path

    def dotlan_path(self, route):
        path = System.objects.get(id=route[0]).name
        for i in range(len(route)-1):
            if G.get_edge_data(route[i], route[i+1])['type'] == 'bridge':
                separator = '::'
            else:
                separator = ':'
            path += (separator + System.objects.get(id=route[i+1]).name)
        path = re.sub(r'(?<!:)(:[^:\s]+)(?=:)(?!::)', '', path)
        return path

    def update_graph(self):
        try:
            G.clear()
            G.add_nodes_from(System.objects.values_list('id', flat=True))
            G.add_edges_from(Gate.objects.values_list('from_system__id', 'to_system__id'), type="gate")
            G.add_edges_from(Bridge.objects.values_list('from_system__id', 'to_system__id'), type="bridge")
        except OperationalError:
            return
        return

    def send_route(self, character, route):
        if settings.SEND_ROUTE:
            for index, id in enumerate(route):
                if index == 0:
                    ESI.request(
                        'post_ui_autopilot_waypoint',
                        client=character.get_client(),
                        add_to_beginning=False,
                        clear_other_waypoints=True,
                        destination_id=id
                    )
                else:
                    ESI.request(
                        'post_ui_autopilot_waypoint',
                        client=character.get_client(),
                        add_to_beginning=False,
                        clear_other_waypoints=False,
                        destination_id=id
                    )
        else:
            print(f'Sending route {route}.')
        return


class Lister:
    def get_lists(self, user):
        try:
            lists = PlannerLists.objects.get(user=user)
        except PlannerLists.DoesNotExist:
            lists = PlannerLists(user=user)
            lists.recents = json.dumps([None] * 5)
            lists.favorites = json.dumps([None] * 5)
            lists.save()
        return json.loads(lists.favorites), json.loads(lists.recents)

    def update_recents(self, user, system):
        lists = PlannerLists.objects.get(user=user)
        recents = json.loads(lists.recents)
        if system not in recents:
            recents.insert(0, system)
            recents.pop()
        else:
            recents.remove(system)
            recents.insert(0, system)
        lists.recents = json.dumps(recents)
        lists.save()
        return json.loads(lists.recents)

    def update_favorites(self, user, favorites):
        lists = PlannerLists.objects.get(user=user)
        lists.favorites = json.dumps(favorites)
        lists.save()
        return json.loads(lists.favorites)
