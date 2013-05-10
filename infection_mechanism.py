
# Note that infection mechanisms do not mutate the underlying +infection_object+,
# they merely return information that allows the +infection_object+ to actually
# infect.
class InfectionMechanism:
    def __init__(self, infection_object):
        self.infection_object = infection_object

    # This class must return the following:
    #
    # (new_infection_nodes, next_frontier, newly_visited)
    #
    # Where +new_infection_nodes+ are the nodes that have just been reached
    # which are not currently infected, but are next to an infected node,
    # +next_frontier+ is the set of nodes that will make up the newest frontier,
    # and +newly_visited+ are the nodes that have just been visited.
    def next_iteration(self):
        raise "Not Implemented"

class BasicInfectionMechanism(InfectionMechanism):
    def next_iteration(self):
        new_infection_nodes = []
        next_frontier = []
        for i in self.infection_object.frontier:
            if self._adjacent_to_infected(i) and i not in self.seen_infection:
                new_infection_nodes.append(i)
            next_frontier.extend(self._frontier_for(i))
        return (new_infection_nodes, next_frontier, newly_visited)

    def _adjacent_to_infected(self, node):
        for i in xrange(self.infection_object.graph.num_nodes):
            if (self.infection_object.graph.adjacency_matrix[node][i] == 1 and
                    self.infection_object.infected_nodes[i] == 1):
                return True
        return False

    def _frontier_for(self, node):
        return [j for j in xrange(self.infection_object.graph.num_nodes) if (
                self.infection_object.graph.adjacency_matrix[node][j] == 1 and
                j not in self.infection_object.seen_infection
                )]



