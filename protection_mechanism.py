from utility_function import *

class ProtectionMechanism:
    def __init__(self, infection_object):
        self.infection_object = infection_object

    def next_iteration(self):
        raise "Not Implemented"

class DynamicProtectionMechanism(ProtectionMechanism):
    def __init__(self, infection_object):
        self.infection_object = infection_object
        self.utility_function = UtilityFunction()
        self.infection_probabilities=[0 for i in xrange(self.infection_object.graph.num_nodes)]
        for i in xrange(self.infection_object.graph.num_nodes):
            self.infection_probabilities[i]=lambda x: self.utility_function.calculate_negative_utility(self._infection_probability_function(self.infection_object.graph.neighbors(i),x),x)


    def next_iteration(self):
        num_nodes = self.infection_object.graph.num_nodes
        new_protection_list = [0 for i in xrange(num_nodes)]
        # for i in self.infection_object.infected_nodes:
        #     if i == 1:
        #         self.infection_object.cure_node(i)
        for i in xrange(num_nodes):
            #print self.infection_object.graph.neighbors(i)
            new_protection_list[i] = self.utility_function.maximize(self.infection_probabilities[i])
        return new_protection_list

    def _infection_probability_function(self, neighbors, protection):
        infection_probability = 1
        for i in neighbors:
            if self.infection_object.infected_nodes[i] == 0:
                infection_probability *= (1 - self.infection_object.attack_probability)
            else:
                infection_probability *= (self.infection_object.cure_probability)
        infection_probability *= (1 - self.infection_object.attack_probability)
        return (1 - infection_probability) * (1 - protection)

