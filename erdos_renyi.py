import graph

class ErdosRenyi:
    def __init__(self, p, num_nodes):
        self.p = p
        self.num_nodes = num_nodes

    def draw_adjacency_matrix(self):
        adjacency_matrix = AdjacencyMatrix(self.num_nodes)
        return self._set_matrix_edges(adjacency_matrix)

    # Mutates the adjacency matrix and sets the matrix according to the
    # probability of set by Erdos Renyi.
    def _set_matrix_edges(self, adjacency_matrix):
        for i in xrange(num_nodes):
            for j in xrange(num_nodes):
                if i <= j and random.random() < self.p:
                    adjacency_matrix.set_edge(i, j)
