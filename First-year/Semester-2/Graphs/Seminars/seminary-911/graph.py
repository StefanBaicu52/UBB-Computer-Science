from random import randint
import time

class Graph:
    def __init__(self, v):
        '''If v is an integer, creates a graph with vertices from 0 to v-1.
            Otherwise, v must be iterable and the function creates a graph with vertices in v
            
        '''
        self._out_edges = {}
        self._in_edges = {}
        self.__cost = {}
        if isinstance(v,int): 
            for i in range(v):
                self._out_edges[i] = []
                self._in_edges[i] = []
        else:
            for i in v:
                self._out_edges[i] = []
                self._in_edges[i] = []

    def add_edge(self, x, y, c=1):
        '''Adds an edge from x to y. Returns False if the edge already exists, True if it was added.
            Precondition: x and y are vertices of the graph
        '''
        if y in self._out_edges[x]:
            return False
        self._out_edges[x].append(y)
        self._in_edges[y].append(x)
        self.__cost[(x,y)] = c
        return True
        

    def is_edge(self, x, y):
        '''Returns True if there is an edge from x to y
            Precondition: x and y are vertices of the graph
        '''
        return y in self._out_edges[x]

    def cost(self, x, y):
        return self.__cost[(x,y)]

    def parse_out(self, x):
        '''Returns an iterable containing all outbound neighbors of x
        '''
        return list(self._out_edges[x])
        #return self._out_edges[x]
#        for y in self._out_edges[x]:
#            yield y

    def parse_in(self, y):
        '''Returns an iterable containing all inbound neighbors of y
        '''
        for x in self._in_edges[y]:
            yield x
#        for x in self._out_edges.keys():
#            if y in self._out_edges[x]:
#                yield x

    def parse_vertices(self):
        '''Returns an iterable containing all vertices of the graph
        '''
        return self._out_edges.keys()

class UndirectedGraph:
    def __init__(self, v):
        '''If v is an integer, creates a graph with vertices from 0 to v-1.
            Otherwise, v must be iterable and the function creates a graph with vertices in v
            
        '''
        self._neighbors = {}
        self.__cost = {}
        if isinstance(v,int): 
            for i in range(v):
                self._neighbors[i] = []
        else:
            for i in v:
                self._neighbors[i] = []

    def add_edge(self, x, y, c=1):
        '''Adds an edge from x to y. Returns False if the edge already exists, True if it was added.
            Precondition: x and y are vertices of the graph
        '''
        if x == y:
            raise Exception("No loops allowed")
        if y in self._neighbors[x]:
            return False
        self._neighbors[x].append(y)
        self._neighbors[y].append(x)
        self.__cost[(x,y)] = c
        self.__cost[(y,x)] = c
        return True
        

    def is_edge(self, x, y):
        '''Returns True if there is an edge from x to y
            Precondition: x and y are vertices of the graph
        '''
        return y in self._neighbors[x]

    def cost(self, x, y):
        return self.__cost[(x,y)]

    def parse_neighbors(self, x):
        '''Returns an iterable containing all outbound neighbors of x
        '''
        return list(self._neighbors[x])

    def parse_out(self, x):
        '''Returns an iterable containing all outbound neighbors of x
        '''
        return self.parse_neighbors(x)

    def parse_in(self, y):
        '''Returns an iterable containing all inbound neighbors of y
        '''
        return self.parse_neighbors(x)

    def parse_vertices(self):
        '''Returns an iterable containing all vertices of the graph
        '''
        return self._neighbors.keys()

def print_graph(g):
    print ("Outbound")
    for x in g.parse_vertices():
        s = f"{x}:"
        for y in g.parse_out(x):
            s += f" {y}"
        print(s)
    print ("Inbound")
    for x in g.parse_vertices():
        s = f"{x}:"
        for y in g.parse_in(x):
            s += f" {y}"
        print(s)

def check_performance(g):
    before = time.time()
    for x in g.parse_vertices():
        for y in g.parse_out(x):
            pass
    after = time.time()
    print(f"Outbound: {(after-before)*1000}ms")
    
    before = time.time()
    for x in g.parse_vertices():
        for y in g.parse_in(x):
            pass
    after = time.time()
    print(f"Inbound: {(after-before)*1000}ms")


def small_test_graph():
    g = Graph(6)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 0, 1)
    g.add_edge(1, 1, 3)
    g.add_edge(1, 3, 1)
    g.add_edge(0, 3, 4)
    g.add_edge(0, 4, 9)
    g.add_edge(5, 4, 3)
    g.add_edge(3, 5, 2)
    g.add_edge(4, 3, 4)
    return g

def small_test_graph_negative_cost():
    g = Graph(6)
    g.add_edge(0, 1, 22)
    g.add_edge(1, 0, 1)
    g.add_edge(1, 1, 3)
    g.add_edge(1, 3, -19)
    g.add_edge(0, 3, 4)
    g.add_edge(0, 4, 9)
    g.add_edge(5, 4, 3)
    g.add_edge(3, 5, 2)
    g.add_edge(4, 3, 4)
    return g

def small_test_graph_negative_cycle():
    g = Graph(6)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 0, 1)
    g.add_edge(1, 1, 3)
    g.add_edge(1, 3, 1)
    g.add_edge(0, 3, 4)
    g.add_edge(0, 4, 9)
    g.add_edge(5, 4, 3)
    g.add_edge(3, 5, 2)
    g.add_edge(4, 3, -6)
    return g

def create_small_dag():
    g = Graph(7)
    g.add_edge(0,6)
    g.add_edge(5,6)
    g.add_edge(5,4)
    g.add_edge(6,1)
    g.add_edge(4,3)
    g.add_edge(6,3)
    g.add_edge(3,2)
    g.add_edge(6,2)
    return g

def get_undirected_graph():
    cost_one = {
        (1,2):1,
        (1,3):2,
        (1,4):3,
        (1,6):2,
        (2,6):1,
        (3,4):4,
        (3,5):3,
        (3,6):2,
        (4,5):1,
        (5,6):5,
    }
    cost = {}
    g = UndirectedGraph(range(1,7))
    for edge in cost_one.keys():
        g.add_edge(*edge, cost_one[edge])
    return g

def random_graph(n, m):
    '''Returns a random graph with n vertices and m edges
    '''
    g = Graph(n)
    for i in range(m):
        result=g.add_edge(randint(0,n-1),randint(0,n-1))
        while result==False:
            result=g.add_edge(randint(0,n-1),randint(0,n-1))
    return g

if __name__ == "__main__":
    #g = small_test_graph()
    #g=random_graph(5,10)
    #lst = g.parse_out(1)
    #lst.remove(0)
    #for x in lst:
    #    print(x)
    #print_graph(g)

    n = 100000
    g=random_graph(n,10*n)
    check_performance(g)
