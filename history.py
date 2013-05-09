import collections

# A class that stores the history of infection on a network.
# In order to use the History class, just initialize it like so:
#
#  history = History(graph.adjacency_matrix)
#  history.set_infection_start(start_node)
#  history.set_infection_object(infection)
#
# Once the history has been set, just make sure to call the +infect+ method
# whenever the infection object makes an infection:
#
#  history.infect(i)
#
# Where +i+ is the node that is infected.
class History:
    def __init__(self, adjacency_matrix = None):
        self.adjacency_matrix = adjacency_matrix
        self.infection_object = None
        self.infection_logs = collections.defaultdict(list)

    def set_infection_object(self, infection_object):
        self.infection_object = infection_object

    def infect(self, node):
        log = InfectionLog(node, "infect", infection_object.current_iteration)
        log.configure_payload(self.infection_object)
        self.infection_logs[infection_object.current_iteration].append(log)

class InfectionLog:
    def __init__(self, node, change_type, iteration):
        self.node = node
        self.change_type = change_type
        self.iteration = iteration
        self.payload = {}

    def configure_payload(self, infection_object):
        if infection_object:
            self.payload["protection"] = infection_object.graph.protection_list[node]
            self.payload["neighbors_infected"] = self._get_infected_neighbors(infection_object)

    def _get_infected_neighbors(self, infection_object):
        infected_neighbors = []
        for i in xrange(infection_object.graph.num_nodes):
            if (infection_object.infected_nodes[i] == 1 and
                infection_object.graph.adjacency_matrix[i] == 1):
                infected_neighbors.append(i)

        return infected_neighbors
