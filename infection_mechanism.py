
# Note that infection mechanisms do not mutate the underlying +infection_object+,
# they merely return information that allows the +infection_object+ to actually
# infect.
class InfectionMechanism:
    def __init__(self, infection_object):
        self.infection_object = infection_object

    # This class must return the following:
    #
    # next_frontier
    #
    # Where +next_frontier+ is the set of nodes that will make up the newest
    # frontier. Note that the newest frontier should only be made up of neighbors
    # of nodes that have newly been infected. It should not contain any nodes 
    # which have already previously seen infection.
    def next_iteration(self):
        raise "Not Implemented"

    def adjacent_to_infected(self, node):
        for i in xrange(self.infection_object.graph.num_nodes):
            if (self.infection_object.graph.adjacency_matrix[node][i] == 1 and 
                    self.infection_object.infected_nodes[i] == 1):
                return True
        return False

class BasicInfectionMechanism(InfectionMechanism):
    def next_iteration(self):
        new_infection_nodes = []
        for i in self.infection_object.frontier:
            for j in self.infection_object.graph.neighbors(i):
                if (self.adjacent_to_infected(j) and
                        j not in self.infection_object.seen_infection):
                    new_infection_nodes.append(j)
        return new_infection_nodes

class DynamicInfectionMechanism(InfectionMechanism):

    def next_interation(self):
        new_infection_nodes = []
        for i in self.infection_object.infected_nodes:
            if i == 0:
                infected = self.infection_object.attack_node(i)
        for i in self.infection_object.infected_nodes:
            for j in self.infection_object.graph.neighbors(i):
                if self.adjacent_to_infected(j) and self.infection_object.infected_nodes[j] == 0:
                    new_infection_nodes.append(j)
        return (new_infection_nodes)

