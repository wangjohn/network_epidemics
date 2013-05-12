

class ProtectionMechanism:
    def __init__(self, infection_object):
        self.infection_object = infection_object

    def next_iteration(self):
        raise "Not Implemented"

class DynamicProtectionMechanism(ProtectionMechanism):
    def __init__(self, infection_object, probability_function):
        self.infection_object = infection_object
        self.utility_function = UtilityFunction()

    def next_iteration(self):
        num_nodes = self.infection_object.graph.num_nodes
        new_protection_list = [0 for i in xrange(num_nodes)]
        for i in self.infection_object.infected_nodes:
            if i == 1:
                self.infection_object.cure_node(i)
        for i in xrange(num_nodes):
            infection_probability = lambda x: self._infection_probability_function(self.infection_object.neighbors(i),x)
            new_protection_list[i] = self.utility_function.maximize(infection_probability)
        return new_protection_list

    def _infection_probability_function(self, neighbors, protection):
        infection_probability = 1
        for i in neighbors:
            if self.infection_object.infected_nodes[i] == 0:
                infection_probability *= (1 - self.infection_object.ATTACK_PROBABILITY)
            else:
                infection_probability *= (self.infection_object.CURE_PROBABILITY)
        infection_probability *= (1 - self.infection_object.ATTACK_PROBABILITY)
        return (1 - infection_probability) * (1 - protection)

