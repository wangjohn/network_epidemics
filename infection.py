import random
import history
import sets
from infection_mechanism import *

# This is a class which plays the game of spreading an infection throughout the
# graph.
#
# If you include a history object, then you can track what happens throughout
# the infection.
class Infection:
    def __init__(self, graph, history = False, infection_mechanism = None,
            protection_mechanism = None, utility_function = None):
        self.graph = graph
        self.current_iteration = 0
        self.frontier = []
        self.seen_infection = sets.Set()
        self.infected_nodes = [0 for i in xrange(self.graph.num_nodes)]

        self._set_infection_mechansim(infection_mechanism)
        self.protection_mechanism = protection_mechanism
        self.utility_function = utility_function
        self._set_history(history)

    def run_infection(self, num_iterations, start_node = "random"):
        self.start_infection(start_node)
        while len(self.frontier) >= 0:
            self.next_iteration()

    def start_infection(self, start_node = "random"):
        start_node = self._get_start_node(start_node)
        self.frontier = [start_node]
        self.infect_node(start_node)

    # Gets the next iteration in the infection on the graph. If we have defined
    # an infection mechanism, then use that to get the next iteration. Otherwise
    # use the simple scheme of infect with probability (1-q) if the disease has
    # reached a neighbor.
    def next_iteration(self):
        self.current_iteration += 1

        # If there is a protection mechnaism, change the protections in each
        # iteration
        if self.protection_mechanism:
            self.graph.protection_list = self.protection_mechanism.next_iteration()
            self.history.change_protection(self.graph.protection_list)

        # Now start infecting with the infection mechanism
        newly_infected_nodes = self.infection_mechanism.next_iteration()
        for node in newly_infected_nodes:
            self.infect_node(node, 1-self.graph.protection_list[node])
        self.frontier = newly_infected_nodes

    # This is the method that should be used whenever you are attempting to
    # infect a node. It makes sure to track the history of infection.
    def infect_node(self, node, probability = 1):
        if node not in self.seen_infection:
            if probability == 1 or random.random() < probability:
                infected = True
                self.infected_nodes[node] = 1
            else:
                infected = False
            self.seen_infection.add(node)
            self._log_infection(node, infected)
            return infected

    def _log_infection(self, node, infected = True):
        if self.history:
            self.history.infect(node, infected)

    # Obtains the start node and does a check to make sure it is an intege, or
    # that it is randomly selected.
    def _get_start_node(self, start_node):
        if start_node == "random":
            return random.uniform(0, self.graph.num_nodes-1)
        elif not isinstance(start_node, int):
            raise Exception("The start node must be an integer or the string 'random'.")

        return start_node

    # Keep a history object which logs each stage of the infection.
    # If the history object is None, then no history will be taken.
    def _set_history(self, history):
        self.history = history
        if self.history:
            self.history = history.History(self, self.graph.adjacency_matrix)

    def _set_infection_mechanism(self, infection_mechanism):
        if infection_mechanism:
            self.infection_mechanism = infection_mechanism
        else:
            self.infection_mechanism = BasicInfectionMechanism(self)


class ComputeInfectionProbabilities:
    def __init__(self, graph):
        self.graph = graph

    def compute(self, protection_list, start_node):
        infection_probabilities = [None for i in xrange(self.graph.num_nodes)]
        infection_probabilities[self.start_node] = 1

        # Fill out the neighbors of the infected node
        for i in self.graph.neighbors(self.start_node):
            infection_probabilities[i] = 1 - protection_list[i]

        # Now create a system of equations
