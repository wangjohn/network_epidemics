import graph
import random

class Game:
    def __init__(self, graph, utility_function, start_node):
        self.graph = graph
        self.utility_function = utility_function
        self.start_node = start_node
        #0 is utility maximizing, 1 is social welfare maximizing
        self.node_types = [0 for n in range(graph.num_nodes)]

    def setFSampling(self, f):
        government_nodes = random.sample(len(self.node_types), floor(f * len(self.node_types)))
        for index in government_nodes:
            self.node_types[index] = 1	

    def setFBernoulli(self, f):
        for i in range(len(self.node_types)):
            if random.random() < f:
                self.node_types[i] = 1

    def setFTopDegree(self, f):
        degree_list = self.graph.degree_list
        top_degree_indices = sorted(range(len(degree_list)), key=lambda i: degree_list[i])[-floor(f*len(degree_list)):]
        for index in top_degree_indices:
            self.node_types[index] = 1

    #assume everyone is of type 0 - selfish type
    def compute_nash(self):
        security_profile = [0 for i in range(len(self.graph.num_nodes))]
        frontier = [self.start_node]
        visited_nodes = []
        while frontier != []
            current_node = frontier.pop()



class Agent:


