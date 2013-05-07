class Graph:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix

class AdjacencyMatrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = [[0 for i in xrange(num_nodes)] for j in xrange(num_nodes)]

    def set_neighbors(self, node, neighbor_list):
        self._check_length(neighbor_list)
        self.matrix[node] = neighbor_list

        # symmetry condition for the undirected graph
        for i in xrange(len(neighbor_list)):
            self.matrix[i] = neighbor_list[i]

    def set_edge(self, node_1, node_2, value = 1):
        self.matrix[node_1][node_2] = value
        self.matrix[node_2][node_1] = value

    def _check_length(self, neighbor_list):
        if len(neighbor_list) != self.num_nodes:
            raise TypeError("The neighbor list is not the correct size")

