import copy
import heapq
from itertools import combinations

class Graph:
    def __init__(self, number_of_vertices, number_of_edges):
        self.__number_of_vertices = number_of_vertices
        self.__number_of_edges = number_of_edges
        self.__incoming_edges = {}
        self.__outgoing_edges = {}
        self.__costs = {}

        for index in range(number_of_vertices):
            self.__incoming_edges[index] = []
            self.__outgoing_edges[index] = []

    @property
    def number_of_vertices(self):
        return self.__number_of_vertices

    @property
    def number_of_edges(self):
        return self.__number_of_edges

    @property
    def incoming_edges(self):
        return self.__incoming_edges

    @property
    def outgoing_edges(self):
        return self.__outgoing_edges

    @property
    def costs(self):
        return self.__costs

    def parse_vertices(self):
        for v in self.__outgoing_edges.keys():
            yield v

    def parse_inbound_edges(self, vertex):
        for y in self.__incoming_edges[vertex]:
            yield y

    def parse_outbound_edges(self, vertex):
        for y in self.__outgoing_edges[vertex]:
            yield y

    def parse_cost(self):
        for key in self.__costs.keys():
            yield key

    def add_vertex(self, vertex):
        if vertex in self.__outgoing_edges or vertex in self.__incoming_edges:
            return False
        self.__outgoing_edges[vertex] = []
        self.__incoming_edges[vertex] = []
        self.__number_of_vertices += 1
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.__outgoing_edges:
            return False

        for v in self.__outgoing_edges:
            if vertex in self.__outgoing_edges[v]:
                self.__outgoing_edges[v].remove(vertex)
        for v in self.__incoming_edges:
            if vertex in self.__incoming_edges[v]:
                self.__incoming_edges[v].remove(vertex)

        self.__outgoing_edges.pop(vertex)
        self.__incoming_edges.pop(vertex)

        for edge in list(self.__costs.keys()):
            if vertex in edge:
                self.__costs.pop(edge)
                self.__number_of_edges -= 1

        self.__number_of_vertices -= 1
        return True

    def add_edge(self, x, y, cost):
        if (x, y) in self.__costs:
            return False
        if x not in self.__outgoing_edges or y not in self.__outgoing_edges:
            return False
        self.__outgoing_edges[x].append(y)
        self.__incoming_edges[y].append(x)
        self.__costs[(x, y)] = cost
        self.__number_of_edges += 1
        return True

    def remove_edge(self, x, y):
        if (x, y) not in self.__costs:
            return False
        self.__outgoing_edges[x].remove(y)
        self.__incoming_edges[y].remove(x)
        self.__costs.pop((x, y))
        self.__number_of_edges -= 1
        return True

    def in_degree(self, vertex):
        if vertex not in self.__incoming_edges:
            return -1
        return len(self.__incoming_edges[vertex])

    def out_degree(self, vertex):
        if vertex not in self.__outgoing_edges:
            return -1
        return len(self.__outgoing_edges[vertex])

    def find_if_edge(self, x, y):
        return self.__costs.get((x, y), False)

    def change_cost(self, x, y, new_cost):
        if (x, y) not in self.__costs:
            return False
        self.__costs[(x, y)] = new_cost
        return True

    def copy_graph(self):
        return copy.deepcopy(self)

    def __bfs_component(self, start_vertex, visited):
        from collections import deque
        queue = deque([start_vertex])
        component = [start_vertex]
        visited.add(start_vertex)

        while queue:
            current = queue.popleft()
            neighbors = set(self.__incoming_edges[current]).union(self.__outgoing_edges[current])
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    component.append(neighbor)
                    queue.append(neighbor)

        return component

    def connected_components_bfs(self):
        visited = set()
        components = []

        for vertex in self.parse_vertices():
            if vertex not in visited:
                component = self.__bfs_component(vertex, visited)
                components.append(component)

        return components

    def dijkstra(self, start_vertex, end_vertex):
        distances = {v: float('inf') for v in self.parse_vertices()}
        previous = {v: None for v in self.parse_vertices()}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.parse_outbound_edges(current_vertex):
                edge = (current_vertex, neighbor)
                weight = self.costs[edge]
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        if distances[end_vertex] == float('inf'):
            return float('inf'), []

        path = []
        current = end_vertex
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        return distances[end_vertex], path

    def check_if_dag_and_toposort(self):
        visited = {}
        stack = []
        has_cycle = False

        def dfs(u):
            nonlocal has_cycle
            if has_cycle:
                return
            visited[u] = 'gray'
            for v in self.outgoing_edges.get(u, []):
                if v not in visited:
                    dfs(v)
                elif visited[v] == 'gray':
                    has_cycle = True
                    return
            visited[u] = 'black'
            stack.append(u)

        for node in self.parse_vertices():
            if node not in visited:
                dfs(node)
            if has_cycle:
                break

        if has_cycle:
            return False, []
        else:
            stack.reverse()
            return True, stack

    def calculate_earliest_latest(self, topo_order):
        earliest_start = {a: 0 for a in self.parse_vertices()}
        latest_start = {a: float('inf') for a in self.parse_vertices()}

        for u in topo_order:
            for v in self.outgoing_edges.get(u, []):
                cost = self.costs.get((u, v), 0)
                earliest_start[v] = max(earliest_start[v], earliest_start[u] + cost)

        project_duration = max([earliest_start[a] for a in self.parse_vertices()] + [0])

        for a in self.parse_vertices():
            if len(self.outgoing_edges.get(a, [])) == 0:
                latest_start[a] = project_duration

        for u in reversed(topo_order):
            for v in self.outgoing_edges.get(u, []):
                cost = self.costs.get((u, v), 0)
                latest_start[u] = min(latest_start[u], latest_start[v] - cost)

        for a in self.parse_vertices():
            if latest_start[a] == float('inf'):
                latest_start[a] = earliest_start[a]

        return earliest_start, latest_start, project_duration

    def get_critical_activities(self, earliest, latest):
        critical = []
        for (u, v), cost in self.costs.items():
            if earliest[u] == latest[u] and earliest[v] == latest[v] and earliest[v] - earliest[u] == cost:
                critical.append((u, v))
        return critical

    def is_vertex_cover(self, subset):
        covered_edges = set()
        for u in self.parse_vertices():
            for v in self.parse_outbound_edges(u):
                if u in subset or v in subset:
                    edge = tuple(sorted((u, v)))  # treat as undirected
                    covered_edges.add(edge)

        total_edges = set()
        for u in self.parse_vertices():
            for v in self.parse_outbound_edges(u):
                edge = tuple(sorted((u, v)))
                total_edges.add(edge)

        return covered_edges >= total_edges

    def minimum_vertex_cover(self):
        vertices = list(self.parse_vertices())
        n = len(vertices)

        for size in range(1, n + 1):
            for subset in combinations(vertices, size):
                if self.is_vertex_cover(set(subset)):
                    return list(subset), size

        return [], 0
