class Graph:
    def __init__(self, adjacency_matrix, protection_list):
        self.num_nodes = adjacency_matrix.num_nodes
        self.adjacency_matrix = adjacency_matrix
        self.protection_list = protection_list

        # Check to make sure the matrices are the right dimensions
        self._check_matching_sizes()

    def neighbors(self, node):
        return [i for i in xrange(len(self.num_nodes)) if self.adjacency_matrix[node][i] == 1]

    # This method checks to make sure that all of the sizes that are defined
    # in the graph are matching. Note that it doesn't do a full check, but it
    # only checks the outside of the matrix.
    def _check_matching_sizes(self):
        if (len(self.adjacency_matrix) != self.num_nodes or
            len(self.protection_list) != self.num_nodes):
            raise Exception("Adjacency and Protection matrix are not the same size")

    def degree_list(self):
        return [sum(self.adjacency_matrix.matrix[i]) for i in range(len(self.num_nodes))]

class AdjacencyMatrix(Matrix):
    def set_edge(self, node_1, node_2, value = 1):
        super(Matrix, self).set_edge(node_1, node_2, value)

# Base implementation of the a matrix. You can set the neighbors of a particular
# node, or the edge between two nodes.
#
# Nodes are represented as integers, and num_nodes provides the number of nodes
# that are in the matrix.
class Matrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = [[0 for i in xrange(num_nodes)] for j in xrange(num_nodes)]

    def set_neighbors(self, node, neighbor_list):
        self._check_length(neighbor_list)
        self.matrix[node] = neighbor_list

        # symmetry condition for the undirected graph
        for i in xrange(len(neighbor_list)):
            self.matrix[i] = neighbor_list[i]

    def set_edge(self, node_1, node_2, value):
        self.matrix[node_1][node_2] = value
        self.matrix[node_2][node_1] = value

    def _check_length(self, neighbor_list):
        if len(neighbor_list) != self.num_nodes:
            raise TypeError("The neighbor list is not the correct size")

