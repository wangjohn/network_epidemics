class Graph:
    def __init__(self, adjacency_matrix, protection_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.protection_matrix = protection_matrix

class ProtectionMatrix(Matrix):
    def __init__(self, num_nodes, cost_function):
        self.cost_function = cost_function
        super(Matrix, self).__init__(num_nodes)

class AdjacencyMatrix(Matrix):
    def set_edge(self, node_1, node_2, value = 1):
        super(Matrix, self).set_edge(node_1, node_2, value)

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

