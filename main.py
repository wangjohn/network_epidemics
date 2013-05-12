import infection
import graph
import erdos_renyi

probability = 0.01
num_nodes = 100
er_generator = erdos_renyi.ErdosRenyi(probability, num_nodes)

graph = graph.Graph(er_generator.draw_adjacency_matrix())

protection_list = [(1.0 / num_nodes) for i in xrange(num_nodes)]
compute_probabilities_object = infection.ComputeInfectionProbabilities(graph, protection_list, 0)

print "Monte Carlo Infection Probabilities:"
print compute_probabilities_object.monte_carlo_compute(1)
