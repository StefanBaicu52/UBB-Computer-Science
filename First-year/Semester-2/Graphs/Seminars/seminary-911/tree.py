import graph

class DisjointSets:
    def __init__(self, elements):
        '''Creates one set of a single object (a singleton) for each object in elements
        '''
        self.__parent = {}
        self.__height = {}
        for element in elements:
            self.__parent[element] = None
            self.__height[element] = 0
    def test_and_join(self, x, y):
        '''If x and y are in distinct sets, it joins the two sets and returns True;
        otherwise, returns False
        '''
        rx = self.__root(x)
        ry = self.__root(y)
        if rx == ry:
            return False
        hx = self.__height[rx]
        hy = self.__height[ry]
        if hx < hy:
            self.__parent[rx] = ry
            del self.__height[rx]
        elif hx > hy:
            self.__parent[ry] = rx
            del self.__height[ry]
        else:
            self.__parent[ry] = rx
            self.__height[rx] += 1
            del self.__height[ry]
        return True

    def __root(self, x):
        if self.__parent[x] is None:
            return x
        return self.__root(self.__parent[x])

def kruskal(g):
    '''Finds the minimum cost spanning tree for graph `g`.
   Returns the list of edges of the tree.
    '''
    edges = []
    for x in g.parse_vertices():
        for y in g.parse_neighbors(x):
            edges.append((x,y))
    edges.sort(key=lambda edge : g.cost(*edge))
    #print(edges)
    tree_edges = []
    components = DisjointSets(g.parse_vertices())
    for x,y in edges:
        if components.test_and_join(x, y):
            tree_edges.append((x,y))
    return tree_edges

def reconstruct_tree(preorder, inorder, tree):
    '''Input: two lists
    Updates the tree as a dictionary {parent: [left, right]} with None for each child that doesn't exist
    Returns the root
    '''
    if len(preorder) < 1 or len(preorder) != len(inorder):
        raise Exception()
    root = preorder[0]
    root_pos = inorder.index(root)
    nr_left = root_pos
    nr_right = len(preorder) - 1 - nr_left
    tree[root] = [None, None]
    if nr_left > 0:
        tree[root][0] = reconstruct_tree(preorder[1:1+nr_left], inorder[0:nr_left], tree)
    if nr_right > 0:
        tree[root][1] = reconstruct_tree(preorder[root_pos+1 : ], inorder[root_pos+1 : ], tree)
    return root

def test_reconstruct_tree():
    preorder = [9, 5, 1, 8, 3, 2, 4, 6, 7]
    inorder  = [1, 8, 5, 9, 4, 2, 6, 3, 7]
    tree = {}
    print(reconstruct_tree(preorder, inorder, tree))
    print(tree)

def test_kruskal():
    g = graph.get_undirected_graph()
    print(kruskal(g))

test_reconstruct_tree()

