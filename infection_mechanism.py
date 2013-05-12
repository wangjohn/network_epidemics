
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

class BasicInfectionMechanism(InfectionMechanism):
    def next_iteration(self):
        new_infection_nodes = []
        next_frontier = []
        previously_infected = list(self.infection_object.infected_nodes)
        for i in self.infection_object.frontier:
            infected = self.infection_object.infect_node(i,
                    1-self.infection_object.graph.protection_list[i])
            next_frontier.append(i) if infected
        return next_frontier

class DynamicInfectionMechanism(InfectionMechanism):

    def next_interation(self):

        for i in self.infection_object.graph.infected_nodes:
            if i==0:
                infected=self.infection_object.new_infect_node(i, self.infection_object.ATTACK_PROBABILITY)



