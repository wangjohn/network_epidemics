import infection
import graph
import erdos_renyi

probability = 0.1
num_nodes = 100
num_trials = 50
er_generator = erdos_renyi.ErdosRenyi(probability, num_nodes)

graph = graph.Graph(er_generator.draw_adjacency_matrix())

protection_list = [0.25 for i in xrange(num_nodes)]
compute_probabilities_object = infection.ComputeInfectionProbabilities(graph, protection_list, 0)

probabilities = compute_probabilities_object.monte_carlo_compute(num_trials)
print "Average Monte Carlo Infection Probabilities", sum(probabilities) / num_nodes
