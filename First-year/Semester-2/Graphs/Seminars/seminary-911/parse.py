import graph
import wolf_goat_cabbage
from heapq import heappush, heappop
import math

def shortest_path(g, start, dest):
    '''Finds the shortes (min length) path from start to dest in graph g.
        Precond: start and dest are vertices in g.
        Returns the path as a list of vertices along it. Returns None if no path exists.
    '''
    return retrive_path(bfs(g,start), dest)
    

def retrive_path(parent, destination):
    if destination not in parent:
        return None
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

def bfs(g, start):
    '''Performs BFS in graph g starting at `start`.
        Returns the tree as a dictionary mapping each vertex to its parent; parent[start] = None
    '''
    idx = 0
    queue = [start]
    parent = {}
    parent[start] = None
    while idx < len(queue):
        current = queue[idx]
        for node in g.parse_out(current):
            if node not in parent.keys():
                parent[node] = current
                queue.append(node)
        idx += 1
    return parent

def min_cost_path_dijkstra(g, start, dest):
    '''Finds the shortes (min length) path from start to dest in graph g.
        Precond: start and dest are vertices in g.
        Returns the path as a list of vertices along it. Returns None if no path exists.
    '''
    parent = dijkstra(g, start, dest)
    return retrive_path(parent, dest)

def dijkstra(g, start, dest=None):
    '''
    '''
    queue = [(0,start)]
    parent = {}
    parent[start] = None
    dist = {start : 0}
    while len(queue) > 0:
        print(f"queue={queue}")
        d,current = heappop(queue)
        if current == dest:
            print("Stop early")
            return parent
        if d > dist[current]:
            print(f"Skipping {current}")
            continue
        print(f"current = {current}")
        for node in g.parse_out(current):
            if node not in dist.keys() or dist[node] > dist[current] + g.cost(current, node):
                dist[node] = dist[current] + g.cost(current, node)
                parent[node] = current
                heappush(queue, (dist[node], node) )
        print(f"dist={dist}, parent={parent}")
    return parent

def min_cost_path_dp(g, start, dest):
    w = [{x : math.inf for x in g.parse_vertices()}]
    w[0][start] = 0
    n = len(w[0])
    for k in range(2*n):
        w_next = {x : math.inf for x in g.parse_vertices()}
        for x in g.parse_vertices():
            for y in g.parse_out(x):
                if w_next[y] > w[k][x] + g.cost(x,y):
                    w_next[y] = w[k][x] + g.cost(x,y)
        w.append(w_next)
    for k in range(len(w)):
        print(f"w[{k}]={w[k]}")
    dist = {x : math.inf for x in g.parse_vertices()}
    for x in dist.keys():
        for k in range(len(w)):
            if dist[x] > w[k][x]:
                dist[x] = w[k][x]
    print(f"dist={dist}")

    if dist[dest] == math.inf:
        return None
    path = []
    current = dest
    while current != start:
        path.append(current)
        for x in g.parse_in(current):
            if dist[x] + g.cost(x, current) == dist[current]:
                current = x
                break
    path.append(start)
    path.reverse()
    return path

def toposort(g):
    '''Performs the topological sorting of graph g.
    Returns the list of vertices in topologically sorted order, or None if thi is impossible.
    '''
    nr_pred = {}
    to_process = []
    for x in g.parse_vertices():
        nr_pred[x] = len(list(g.parse_in(x)))
        if nr_pred[x] == 0:
            to_process.append(x)
    sorted = []
    while len(to_process) > 0:
        #print(f"nr_pred={nr_pred}")
        #print(f"to_process={to_process}")
        x = to_process.pop()
        #print(f"x={x}")
        sorted.append(x)
        for y in g.parse_out(x):
            nr_pred[y] -= 1
            if nr_pred[y] == 0:
                to_process.append(y)
    #print(f"nr_pred={nr_pred}")
    if len(sorted) < len(nr_pred):
        print(f"cycle={find_cycle(g, nr_pred)}")
        return None
    return sorted

def find_cycle(g, nr_pred):
    for x in nr_pred.keys():
        if nr_pred[x] != 0:
            start = x
            break
    current = start
    cycle = [start]
    visited = set(cycle)
    while True:
        for x in g.parse_in(current):
            if nr_pred[x] != 0:
                current = x
                break
        if current in visited:
            pos = 0
            while cycle[pos] != current:
                pos += 1
            cycle = list(cycle[pos:])
            cycle.append(current)
            cycle.reverse()
            return cycle
        cycle.append(current)
        visited.add(current)

def toposort2(g):
    visited = set()
    on_stack = set()
    sorted = []
    for x in g.parse_vertices():
        if x not in visited:
            ret = toposort_dfs(x, g, visited, on_stack, sorted)
            if ret is not None:
                print(f"Cycle={ret}")
                return None
    return sorted

def toposort_dfs(x, g, visited, on_stack, sorted):
    visited.add(x)
    on_stack.add(x)
    for y in g.parse_in(x):
        if y in on_stack:
            return [y, x]
        if y not in visited:
            ret = toposort_dfs(y, g, visited, on_stack, sorted)
            if ret is not None:
                if ret[0] == ret[-1]:
                    return ret
                else:
                    ret. append(x)
                    return ret
    sorted.append(x)
    on_stack.remove(x)
    return None

def longest_path(g):
    max_len = {}
    prev = {}
    max_len_all = -1
    last = None
    # max_len[x] = length of max length path ending in x
    for x in toposort(g):
        max_len[x] = 0
        prev[x] = None
        for y in g.parse_in(x):
            if max_len[y] + 1 > max_len[x]:
                max_len[x] = max_len[y] + 1
                prev[x] = y
        if max_len[x] > max_len_all:
            max_len_all = max_len[x]
            last = x
    print(f"max_len={max_len}, prev={prev}")
    print(f"max_len_all={max_len_all}, last={last}")
    return retrive_path(prev, last)

def longest_path_rec(x, g, max_len, prev):
    '''Computes the longest path ending in x, together with the previous vertex before it
    '''
    if x in max_len.keys():
        return
    max_len_x = 0
    prev_x = None
    for y in g.parse_in(x):
        longest_path_rec(y, g, max_len, prev)
        if max_len_x < max_len[y] + 1:
            max_len_x = max_len[y] + 1
            prev_x = y
    max_len[x] = max_len_x
    prev[x] = prev_x

def longest_path2(g):
    max_len = {}
    prev = {}
    max_len_all = -1
    last = None
    for x in g.parse_vertices():
        longest_path_rec(x, g, max_len, prev)
        if max_len[x] > max_len_all:
            max_len_all = max_len[x]
            last = x
    print(f"max_len={max_len}, prev={prev}")
    print(f"max_len_all={max_len_all}, last={last}")
    return retrive_path(prev, last)

def compute_scheduling(g, duration):
    '''Given the activity dependency graph `g` and the duration `duration[x]` for each activity,
    computes and returns a tuple (earliest_start, latest_start, critical) where `earliest_start` and `latest_start` are
    dictionaries mapping each activity to its start time for the earliest and for the latest scheduling, and `critical` is the
    list of critical activities
    '''
    sorted = toposort(g)
    earliest_start = {}
    earliest_finish = {}
    project_duration = 0
    for x in sorted:
        earliest_start[x] = 0
        for y in g.parse_in(x):
            if earliest_finish[y] > earliest_start[x]:
                earliest_start[x] = earliest_finish[y]
        earliest_finish[x] = earliest_start[x] + duration[x]
        if earliest_finish[x] > project_duration:
            project_duration = earliest_finish[x]
    latest_start = {}
    latest_finish = {}
    critical = []
    project_start = None
    for x in reversed(sorted):
        latest_finish[x] = project_duration
        for y in g.parse_out(x):
            if latest_finish[x] > latest_start[y]:
                latest_finish[x] = latest_start[y]
        latest_start[x] = latest_finish[x] - duration[x]
        if latest_start[x] == earliest_start[x]:
            critical.append(x)
        if project_start is None or project_start > latest_start[x]:
            project_start = latest_start[x]
    if project_start != 0:
        raise Exception("This should not happen")
    return (earliest_start, latest_start, critical)

def test1():
    g = graph.small_test_graph()
    graph.print_graph(g)
    print(bfs(g, 0))
    print(bfs(g,1))
    print(shortest_path(g, 0, 3))
    print(shortest_path(g, 3, 2))

def test2():
    g = wolf_goat_cabbage.WolfGoatCabbageGraph()
    s = g.initial_state()
    t = g.final_state()
    print(s)
    print(t)
    path = shortest_path(g, s, t)
    print(path)

def test_dijkstra():
    g = graph.small_test_graph()
    print(min_cost_path_dijkstra(g, 0, 4))

def test_dp():
    g = graph.small_test_graph()
    print(min_cost_path_dp(g, 0, 4))
    
def test_dag():
    g = graph.create_small_dag()
    #g.add_edge(1,0)
    #print(toposort2(g))
    print(longest_path2(g))

def test_scheduling():
    g = graph.create_small_dag()
    duration = {0:1, 5:2, 6:5, 4:1, 1:2, 3:2, 2:1}
    print(compute_scheduling(g, duration))

test_dag()
