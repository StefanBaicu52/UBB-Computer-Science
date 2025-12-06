from random import randint
from graph import Graph

def write_graph_to_file(graph, filename):
    with open(filename, "w") as file:
        if graph.number_of_edges and graph.number_of_vertices:
            file.write(f"{graph.number_of_vertices} {graph.number_of_edges}\n")
            if not graph.costs:
                raise ValueError("Graph is empty")
            for key in graph.costs:
                file.write(f"{key[0]} {key[1]} {graph.costs[key]}\n")
        else:
            file.write("We cannot create this graph\n")

def read_graph_from_file(filename):
    with open(filename, "r") as file:
        line = file.readline().strip()
        vertices, edges = line.split(' ')
        graph = Graph(int(vertices), int(edges))
        for v in range(graph.number_of_vertices):
            graph.incoming_edges[v] = []
            graph.outgoing_edges[v] = []

        for line in file:
            parts = line.strip().split(' ')
            if len(parts) == 3:
                x, y, cost = map(int, parts)
                graph.outgoing_edges[x].append(y)
                graph.incoming_edges[y].append(x)
                graph.costs[(x, y)] = cost

        graph._Graph__number_of_edges = len(graph.costs)
    return graph

class UI:
    def __init__(self):
        self._graphs = []
        self._current = None

    def generate_random(self, vertices, edges):
        graph = Graph(vertices, 0)
        i = 0
        while i < edges:
            x = randint(0, vertices - 1)
            y = randint(0, vertices - 1)
            cost = randint(0, 500)
            if graph.add_edge(x, y, cost):
                i += 1
        return graph

    def switch_graph_ui(self):
        print(f"You are on the graph number: {self._current}")
        print(f"Available graphs: from 0 to {len(self._graphs) - 1}")
        number = int(input("Enter the graph number you want to switch to: "))
        if not 0 <= number < len(self._graphs):
            raise ValueError("Invalid graph index!")
        self._current = number

    def add_empty_graph(self):
        graph = Graph(0, 0)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def create_random_graph_ui(self):
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of edges: "))
        if edges > vertices * (vertices - 1):
            print("Too many edges!")
            return
        graph = self.generate_random(vertices, edges)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def find_lowest_cost_walk_ui(self):
        start = int(input("Enter the starting vertex: "))
        end = int(input("Enter the ending vertex: "))
        if start not in self._graphs[self._current].parse_vertices() or end not in self._graphs[self._current].parse_vertices():
            print("One or both vertices do not exist in the graph.")
            return
        cost, path = self._graphs[self._current].dijkstra(start, end)
        if cost == float('inf'):
            print(f"No path from {start} to {end}.")
        else:
            print(f"Lowest cost path: {' -> '.join(map(str, path))}")
            print(f"Total cost: {cost}")

    def activity_scheduling_ui(self):
        graph = self._graphs[self._current]
        is_dag, topo_order = graph.check_if_dag_and_toposort()
        if not is_dag:
            print("The graph is not a DAG.")
            return
        earliest, latest, total = graph.calculate_earliest_latest(topo_order)
        print("Earliest and Latest Start Times:")
        for a in topo_order:
            print(f"Activity {a}: Earliest = {earliest[a]}, Latest = {latest[a]}")
        print(f"Total project duration: {total}")
        critical = graph.get_critical_activities(earliest, latest)
        print("Critical activities (zero slack):", critical)

    def get_number_of_vertices_ui(self):
        print(f"The number of vertices is: {self._graphs[self._current].number_of_vertices}")

    def get_number_of_edges_ui(self):
        print(f"The number of edges is: {self._graphs[self._current].number_of_edges}")

    def list_all_outbound(self):
        for x in self._graphs[self._current].parse_vertices():
            print(f"{x} :", ' '.join(map(str, self._graphs[self._current].parse_outbound_edges(x))))

    def list_outbound(self):
        vertex = int(input("Enter the vertex: "))
        if vertex not in self._graphs[self._current].parse_vertices():
            raise ValueError("Vertex does not exist.")
        print(f"{vertex} :", ' '.join(f"({vertex}, {y})" for y in self._graphs[self._current].parse_outbound_edges(vertex)))

    def list_all_inbound(self):
        for x in self._graphs[self._current].parse_vertices():
            print(f"{x} :", ' '.join(map(str, self._graphs[self._current].parse_inbound_edges(x))))

    def list_inbound(self):
        vertex = int(input("Enter the vertex: "))
        if vertex not in self._graphs[self._current].parse_vertices():
            raise ValueError("Vertex does not exist.")
        print(f"{vertex} :", ' '.join(f"({y}, {vertex})" for y in self._graphs[self._current].parse_inbound_edges(vertex)))

    def list_all_costs(self):
        for key in self._graphs[self._current].parse_cost():
            print(f"({key[0]}, {key[1]}) : {self._graphs[self._current].costs[key]}")

    def parse_all_vertices(self):
        for vertex in self._graphs[self._current].parse_vertices():
            print(vertex)

    def add_vertex_ui(self):
        vertex = int(input("Enter vertex: "))
        if self._graphs[self._current].add_vertex(vertex):
            print("Vertex added.")
        else:
            print("Vertex already exists.")

    def delete_vertex_ui(self):
        vertex = int(input("Enter vertex to delete: "))
        if self._graphs[self._current].remove_vertex(vertex):
            print("Vertex deleted.")
        else:
            print("Vertex does not exist.")

    def add_edge_ui(self):
        x = int(input("Enter source vertex: "))
        y = int(input("Enter target vertex: "))
        cost = int(input("Enter cost: "))
        if self._graphs[self._current].add_edge(x, y, cost):
            print("Edge added.")
        else:
            print("Edge already exists or invalid vertices.")

    def remove_edge_ui(self):
        x = int(input("Enter source vertex: "))
        y = int(input("Enter target vertex: "))
        if self._graphs[self._current].remove_edge(x, y):
            print("Edge removed.")
        else:
            print("Edge does not exist.")

    def modify_cost_ui(self):
        x = int(input("Enter source vertex: "))
        y = int(input("Enter target vertex: "))
        cost = int(input("Enter new cost: "))
        if self._graphs[self._current].change_cost(x, y, cost):
            print("Cost updated.")
        else:
            print("Edge not found.")

    def get_in_degree_ui(self):
        v = int(input("Enter vertex: "))
        print("In-degree:", self._graphs[self._current].in_degree(v))

    def get_out_degree_ui(self):
        v = int(input("Enter vertex: "))
        print("Out-degree:", self._graphs[self._current].out_degree(v))

    def check_if_edge_ui(self):
        x = int(input("Source vertex: "))
        y = int(input("Target vertex: "))
        cost = self._graphs[self._current].find_if_edge(x, y)
        if cost is not False:
            print(f"Edge exists with cost {cost}.")
        else:
            print("Edge does not exist.")

    def copy_current_graph_ui(self):
        self._graphs.append(self._graphs[self._current].copy_graph())
        print("Graph copied.")

    def read_graph_from_file_ui(self):
        filename = input("Filename: ")
        graph = read_graph_from_file(filename)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1
        print("Graph loaded from file.")

    def write_graph_to_file_ui(self):
        file = f"graph{self._current}.txt"
        write_graph_to_file(self._graphs[self._current], file)
        print(f"Graph written to {file}.")

    def write_modified_graph_to_file_ui(self):
        file = f"graph_modif{self._current}.txt"
        write_graph_to_file(self._graphs[self._current], file)
        print(f"Modified graph written to {file}.")

    def show_connected_components_ui(self):
        components = self._graphs[self._current].connected_components_bfs()
        for i, component in enumerate(components):
            print(f"Component {i+1}: {component}")

    def minimum_vertex_cover_ui(self):
        graph = self._graphs[self._current]
        cover, size = graph.minimum_vertex_cover()
        print(f"Minimum Vertex Cover (size {size}): {cover}")

    def print_menu(self):
        print("""
                ========== Graph Menu ==========
                0. Exit
                1. Create random graph
                2. Load graph from file
                3. Save graph to file
                4. Switch current graph
                5. Add empty graph
                6. Number of vertices
                7. Number of edges
                8. In-degree of a vertex
                9. Out-degree of a vertex
                10. List all vertices
                11. Add vertex
                12. Remove vertex
                13. Add edge
                14. Remove edge
                15. Modify edge cost
                16. Outbound edges of a vertex
                17. All outbound edges
                18. Inbound edges of a vertex
                19. All inbound edges
                20. Edge costs
                21. Check if edge exists
                22. Copy current graph
                23. Save modified graph to file
                24. Show connected components
                25. Find lowest cost path (Dijkstra)
                26. Activity scheduling (CPM)
                27. Find minimum vertex cover
                ===============================
        """)

    def start(self):
        print("Welcome to Graph Manager!")
        self.add_empty_graph()
        command_dict = {
            "1": self.create_random_graph_ui,
            "2": self.read_graph_from_file_ui,
            "3": self.write_graph_to_file_ui,
            "4": self.switch_graph_ui,
            "5": self.add_empty_graph,
            "6": self.get_number_of_vertices_ui,
            "7": self.get_number_of_edges_ui,
            "8": self.get_in_degree_ui,
            "9": self.get_out_degree_ui,
            "10": self.parse_all_vertices,
            "11": self.add_vertex_ui,
            "12": self.delete_vertex_ui,
            "13": self.add_edge_ui,
            "14": self.remove_edge_ui,
            "15": self.modify_cost_ui,
            "16": self.list_outbound,
            "17": self.list_all_outbound,
            "18": self.list_inbound,
            "19": self.list_all_inbound,
            "20": self.list_all_costs,
            "21": self.check_if_edge_ui,
            "22": self.copy_current_graph_ui,
            "23": self.write_modified_graph_to_file_ui,
            "24": self.show_connected_components_ui,
            "25": self.find_lowest_cost_walk_ui,
            "26": self.activity_scheduling_ui,
            "27": self.minimum_vertex_cover_ui
        }

        while True:
            try:
                self.print_menu()
                cmd = input("Enter command: ")
                if cmd == "0":
                    print("Goodbye!")
                    break
                elif cmd in command_dict:
                    command_dict[cmd]()
                else:
                    print("Invalid command.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    UI().start()
