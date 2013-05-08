import graph

# Class for creating an Erdos Renyi adjacency matrix. Usage is as follows:
#
#  probability = 0.01
#  num_nodes = 5000
#  er_generator = ErdosRenyi(probability, num_nodes)
#
#  # now generate 50 erdos renyi graphs
#  matrices = []
#  for i in xrange(50):
#       matrices.append(er_generator.draw_agencency_matrix())
#
# The +draw_adjacency_matrix+ method will create new adjacency matrices based
# on the probability and number of nodes of the underlying object.
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
