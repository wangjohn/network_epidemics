import random
import history as hist
import sets
import verbose
from infection_mechanism import *
from protection_mechanism import *

# This is a class which plays the game of spreading an infection throughout the
# graph.
#
# If you include a history object, then you can track what happens throughout
# the infection.
class Infection:
    def __init__(self, graph, protection_list, history = False,
            infection_mechanism = None,
            protection_mechanism = None,
            attack_probability = 0.0,
            cure_probability = 0.0,
            debug = True):
        self.graph = graph
        self.protection_list = protection_list
        self.current_iteration = 0
        self.frontier = []
        self.seen_infection = sets.Set()
        self.infected_nodes = [0 for i in xrange(self.graph.num_nodes)]

        self.attack_probability = attack_probability
        self.cure_probability = cure_probability

        self._set_infection_mechanism(infection_mechanism)
        self._set_protection_mechanism(protection_mechanism)
        self._set_history(history)
        self.verbose = verbose.Verbose(debug)

    def run_infection(self, start_node = "random", max_iterations = 50):
        self.start_infection(start_node)
        while len(self.frontier) >= 0 and self.current_iteration < max_iterations:
            #print self.current_iteration
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
            self.protection_list = self.protection_mechanism.next_iteration()
            if self.history:
                self.history.change_protection(self.protection_list)

        # Now start infecting with the infection mechanism
        newly_infected_nodes = set(self.infection_mechanism.next_iteration())
        for node in newly_infected_nodes:
            self.infect_node(node)
        self.frontier = newly_infected_nodes

    # This is the method that should be used whenever you are attempting to
    # infect a node. It makes sure to track the history of infection.
    def infect_node(self, node, probability = None):
        if node not in self.seen_infection:
            self.perform_infection(node, probability)

    # Performs either an infection or a cure (relying on the fact that booleans
    # are just stored as integers). If +probability+ is not defined, then the
    # probability defaults to the infection probability of the +node+. If
    # +infected+ is not set, then this method defaults to performing an 
    # infection instead of a cure.
    def perform_infection(self, node, probability = None, infected = False):
        if not probability:
            probability = 1 - self.protection_list[node]

        if probability == 1 or random.random() < probability:
            infected = not infected
            self.infected_nodes[node] = infected

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
            self.history = hist.History(self, self.graph.adjacency_matrix)

    # defaults to basic, unless specified to dynamic
    def _set_infection_mechanism(self, infection_mechanism):
        if infection_mechanism == "dynamic":
            self.infection_mechanism = DynamicInfectionMechanism(self)
        else:
            self.infection_mechanism = BasicInfectionMechanism(self)

    # sets to protection mechanism if there is one
    def _set_protection_mechanism(self, protection_mechanism):
        if protection_mechanism == "dynamic":
            self.protection_mechanism = DynamicProtectionMechanism(self)
        else:
            self.protection_mechanism = None

class ComputeInfectionProbabilities:
    def __init__(self, graph, protection_list, start_node,
            infection_mechanism = None,
            protection_mechanism = None,
            attack_probability = 0.0,
            cure_probability = 0.0):
        self.graph = graph
        self.protection_list = protection_list
        self.start_node = start_node

        self.infection_mechanism = infection_mechanism
        self.protection_mechanism = protection_mechanism
        self.attack_probability = attack_probability
        self.cure_probability = cure_probability

        # Storage list for the probabilities of infection
        self.infection_probabilities = [None for i in xrange(self.graph.num_nodes)]
        self.infection_probabilities[self.start_node] = 1

        for i in self.graph.neighbors(self.start_node):
            self.infection_probabilities[i] = 1 - self.protection_list[i]

    def monte_carlo_compute(self, num_trials):
        protection_list_sum = [0 for i in xrange(self.graph.num_nodes)]

        for i in xrange(num_trials):
            infection_object = Infection(self.graph, self.protection_list,
                    infection_mechanism = self.infection_mechanism,
                    protection_mechanism = self.protection_mechanism,
                    attack_probability = self.attack_probability,
                    cure_probability = self.cure_probability)
            infection_object.run_infection(self.start_node)
            protection_list_sum = [sum(a) for a in zip(protection_list_sum, infection_object.infected_nodes)]

        return protection_list_sum

    def monte_carlo_compute_summary(self, num_trials):
        protection_list_sum = self.monte_carlo_compute(num_trials)
        computed_probability = float(sum(protection_list_sum)) / (num_trials * len(protection_list_sum))
        estimated_std = self._compute_std(computed_probability, num_trials)
        return (computed_probability, estimated_std)

    def _compute_std(self, computed_probability, num_trials):
        return (0.5 * computed_probability * (1 - computed_probability) / num_trials) ** (0.5)

    def _initialize_infection_probabilities(self, initialize_neighbors = True):
        # Storage list for the probabilities of infection
        self.infection_probabilities = [None for i in xrange(self.graph.num_nodes)]
        self.infection_probabilities[self.start_node] = 1

        if initialize_neighbors:
            for i in self.graph.neighbors(self.start_node):
                self.infection_probabilities[i] = 1 - self.protection_list[i]
