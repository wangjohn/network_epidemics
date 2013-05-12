import infection
import graph
import erdos_renyi

def compute_average_probability(graph, protection_range, num_trials = 250):
    probabilities_hash = {}
    protection_string = "{:15s} {:15s} {:15s}"
    print protection_string.format("Protection", "Probability", "Network Effect")
    for q in protection_range:
        protection_list = [q for i in xrange(graph.num_nodes)]
        compute_probabilities_object = infection.ComputeInfectionProbabilities(graph, protection_list, 0)

        probabilities = compute_probabilities_object.monte_carlo_compute(num_trials)
        probabilities_hash[q] = sum(probabilities) / num_nodes
        protection_string.format(str(q), str(probabilities_hash[q]), str(1 - q - probabilities_hash[q]))
    return probabilities_hash


if __name__ == '__main__':
    erdos_edge_probability = 0.1
    num_nodes = 100
    er_generator = erdos_renyi.ErdosRenyi(erdos_edge_probability, num_nodes)
    graph = graph.Graph(er_generator.draw_adjacency_matrix())
    protection_range = [float(i)/100 for i in xrange(5, 100, 5)]

    print compute_average_probability(graph, protection_range)
