import random

# This is a class which plays the game of spreading an infection throughout the
# graph.
#
class Infection:
    def __init__(self, graph, infection_mechanism = None, history = None):
        self.graph = graph
        self.current_iteration = 0
        self.infected_nodes = [0 for i in xrange(self.graph.num_nodes)]
        self.infection_mechanism = infection_mechanism

        # Keep a history object which logs each stage of the infection.
        # If the history object is None, then no history will be taken.
        self.history = history

    def start_infection(self, start_node = "random"):
        start_node = self._get_start_node(start_node)
        self._infect_node(self, start_node)

    # Gets the next iteration in the infection on the graph. If we have defined
    # an infection mechanism, then use that to get the next iteration. Otherwise
    # use the simple scheme of infect with probability (1-q) if the disease has
    # reached a neighbor.
    def next_iteration(self):
        if infection_mechanism:
            self.infection_mechanism.next_iteration(self)
        else:
            for i in xrange(self.graph.num_nodes):
                if self._sterile_but_adjacent_to_infected(i):
                    self._infect_node(i, 1-self.graph.protection_list[i])

    def _infect_node(self, node, probability = 1):
        if probability == 1 or probability < random.random():
            self.history.infect(node, self.current_iteration)
            self.infected_nodes[node] = 1

    # Returns true if node has not yet been infected but is adjacent to an
    # infected node, false otherwise.
    def _sterile_but_adjacent_to_infected(self, node):
        if self.infected_nodes[node] == 1:
            return False

        # Check to see if a neighbor is infected
        for neighbor in xrange(self.graph.num_nodes):
            if self.graph.adjacency_matrix[node][neighbor] == 1 and
                self.infected_nodes[neighbor] == 1:
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
