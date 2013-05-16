import graph
import random
import math

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
        adjacency_matrix = graph.AdjacencyMatrix(self.num_nodes)
        for i in xrange(self.num_nodes):
            for j in xrange(self.num_nodes):
                if i <= j and random.random() < self.p:
                    adjacency_matrix.set_edge(i, j)

        return adjacency_matrix

class PreferentialAttachment:
    # k <= num_nodes
    def __init__(self, k, num_nodes):
        self.k = k
        self.num_nodes = num_nodes

    def draw_adjacency_matrix(self):
        adjacency_matrix = graph.AdjacencyMatrix(self.num_nodes)
        stubs = {}
        k=0
        for i in xrange(self.k):
            for j in xrange(self.k):
                adjacency_matrix.set_edge(i,j)
                stubs[k]=i
                k+=1
                stubs[k]=j
                k+=1
        for i in xrange(self.k, self.num_nodes):
            for m in xrange(self.k):
                j=stubs[math.floor(random.random()*k)]
                adjacency_matrix.set_edge(i,j)
                stubs[k]=i
                k+=1
                stubs[k]=j
                k+=1

        return adjacency_matrix




