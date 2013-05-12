import infection
import graph
import erdos_renyi

def compute_average_probability(graph, protection_range, num_trials = 250):
    probabilities_hash = {}
    protection_string = "{:15s} {:15s} {:15s} {:15s}"
    print protection_string.format("Protection", "Probability", "Standard Dev", "Network Effect")
    for q in protection_range:
        protection_list = [q for i in xrange(graph.num_nodes)]
        compute_probabilities_object = infection.ComputeInfectionProbabilities(graph, protection_list, 0)

        prob, std = compute_probabilities_object.monte_carlo_compute_summary(num_trials)
        probabilities_hash[q] = prob
        print protection_string.format(str(q), str(prob), str(std), str(1 - q - prob))
    return probabilities_hash

def generate_and_test_graphs(erdos_parameters_range, protection_range, graph_generations = 5):
    for (prob, nodes) in erdos_parameters_range:
        er_generator = erdos_renyi.ErdosRenyi(prob, nodes)
        print "Erdos Renyi, p = %s, n = %s" % (prob, nodes)
        for i in xrange(graph_generations):
            current_graph = graph.Graph(er_generator.draw_adjacency_matrix())

            print "Erdos Renyi, p = %s, n = %s, Graph %s" % (prob, nodes, i)
            compute_average_probability(current_graph, protection_range)

if __name__ == '__main__':
    erdos_parameters_range = [(0.05, 100), (0.1, 100), (0.15, 100), (0.20, 100), (0.25, 100)]
    protection_range = [float(i)/100 for i in xrange(5, 100, 5)]

    generate_and_test_graphs(erdos_parameters_range, protection_range)
