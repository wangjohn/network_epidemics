import random
import history

# This is a class which plays the game of spreading an infection throughout the
# graph.
#
# If you include a history object, then you can track what happens throughout
# the infection.
class Infection:
    def __init__(self, graph, history = False, infection_mechanism = None,
            protection_mechanism = None):
        self.graph = graph
        self.current_iteration = 0
        self.infected_nodes = [0 for i in xrange(self.graph.num_nodes)]
        self.infection_mechanism = infection_mechanism
        self.protection_mechanism = protection_mechanism

        self._set_history(history)

    def run_infection(self, num_iterations, start_node = "random"):
        self.start_infection(start_node)
        for iteration in xrange(num_iterations):
            self.next_iteration()

    def start_infection(self, start_node = "random"):
        start_node = self._get_start_node(start_node)
        self._infect_node(start_node, start_node = True)

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

        # Now start infecting (if we don't have an infection mechanism, use the 
        # default mechanism)
        if self.infection_mechanism:
            self.infection_mechanism.next_iteration()
        else:
            for i in xrange(self.graph.num_nodes):
                if self._sterile_but_adjacent_to_infected(i):
                    self._infect_node(i, 1-self.graph.protection_list[i])

    # This is the method that should be used whenever you are attempting to
    # infect a node. It makes sure to track the history of infection.
    def infect_node(self, node, probability = 1):
        if probability == 1 or random.random() < probability:
            self._log_infection(node)
            self.infected_nodes[node] = 1

    def _log_infection(self, node):
        if self.history:
            self.history.infect(node)

    # Returns true if node has not yet been infected but is adjacent to an
    # infected node, false otherwise.
    def _sterile_but_adjacent_to_infected(self, node):
        if self.infected_nodes[node] == 1:
            return False

        # Check to see if a neighbor is infected
        for neighbor in xrange(self.graph.num_nodes):
            if (self.graph.adjacency_matrix[node][neighbor] == 1 and
                self.infected_nodes[neighbor] == 1):
                  return True
        return False

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
