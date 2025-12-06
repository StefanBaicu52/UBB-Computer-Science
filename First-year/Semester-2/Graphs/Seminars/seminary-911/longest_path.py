import graph

from collections import deque
import time

def get_graph_for_longest_path():
    edges = [
        (0,1),
        (0,2),
        (1,2),
        (1,3),
        (2,1),
        (2,4),
        (3,4),
    ]
    cost = {}
    g = graph.Graph(range(5))
    for edge in edges:
        g.add_edge(*edge)
    return g

def complete_graph(n):
    g = graph.Graph(range(n))
    for x in range(n):
        for y in range(n):
            g.add_edge(x, y)
    return g

def longest_path_backtracking(g, s):
    '''Returns the longest path starting from vertex `s` in graph `g` (as a list of vertices)
    '''
    best_sol = [s]
    longest_path_rec([s], g, best_sol)
    return best_sol
    
def longest_path_rec(prefix, g, best_sol):
    #print(f"prefix = {prefix}")
    if len(prefix) > len(best_sol):
        best_sol.clear()
        best_sol.extend(prefix)
    for x in g.parse_out(prefix[-1]):
        if x not in prefix:
            prefix.append(x)
            longest_path_rec(prefix, g, best_sol)
            prefix.pop()

def longest_path_backtracking2(g, s):
    '''Returns the longest path starting from vertex `s` in graph `g` (as a list of vertices)
    '''
    return longest_path_rec2([s], g)
    
def longest_path_rec2(prefix, g):
    #print(f"prefix = {prefix}")
    # time:O(n!*n); space: O(n)
    best_sol = list(prefix)
    for x in g.parse_out(prefix[-1]):
        if x not in prefix:
            prefix.append(x)
            tmp = longest_path_rec2(prefix, g)
            if len(tmp) > len(best_sol):
                best_sol = tmp
            prefix.pop()
    return best_sol


def longest_path_bb(g, s):
    # time:O(n!*n); space: O(n!)
    q = deque()
    q.append([s])
    best_path = [s]
    while len(q) > 0:
        path = q.popleft()
        #print(f"Path={path}")
        if len(path) > len(best_path):
            best_path = path
        for x in g.parse_out(path[-1]):
            if x not in path:
                new_path = path + [x]
                q.append(new_path)
    return best_path

def longest_path_dp(g, s):
    # similar to w[k,x] = cost of the min cost walk from s to x of length = k
    # prev[k][A, x] = previous vertex just before x on the max len path form s to x of length = k using vertices in A (k = |A| - 1)
    # time: O(2^n * n^2); space: O(2^n * n)
    n = len(list(g.parse_vertices()))
    prev = [{(frozenset([s]), s) : None}]
    best_entry = None
    for k in range(1, n):
        prev.append({})
        for vertices,last_vertex in prev[k-1].keys():
            for next_vertex in g.parse_out(last_vertex):
                if next_vertex not in vertices:
                    new_set = set(vertices)
                    new_set.add(next_vertex)
                    prev[k][frozenset(new_set), next_vertex] = last_vertex
                    best_entry = (frozenset(new_set), next_vertex)
    #print(f"prev={prev}")
    #print(f"best_entry={best_entry}")
    path = []
    vertices, last_vertex = best_entry
    while last_vertex is not None:
        path.append(last_vertex)
        prev_vertex = prev[len(vertices)-1][vertices, last_vertex]
        tmp = set(vertices)
        tmp.remove(last_vertex)
        vertices = frozenset(tmp)
        last_vertex = prev_vertex
    path.reverse()
    return path

def test_longest_path():
    #g = get_graph_for_longest_path()
    g = complete_graph(20)
    before = time.time()
    #result = longest_path_backtracking2(g, 0)
    #result = longest_path_bb(g, 0)
    result = longest_path_dp(g, 0)
    after = time.time()
    print(f"Result = {result}")
    print(f"Time = {after-before}")

test_longest_path()
