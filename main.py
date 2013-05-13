import infection
import graph
import erdos_renyi
import result_keeper

def compute_average_probability(graph, protection_range, result_history, num_trials = 250):
    protection_string = "{:15s} {:15s} {:15s} {:15s}"
    print protection_string.format(*result_history.headers)
    for q in protection_range:
        protection_list = [q for i in xrange(graph.num_nodes)]
        compute_probabilities_object = infection.ComputeInfectionProbabilities(graph, protection_list, 0)

        prob, std = compute_probabilities_object.monte_carlo_compute_summary(num_trials)
        result_history.append([q, prob, std, 1-q-prob], graph)
        print protection_string.format(str(q), str(prob), str(std), str(1 - q - prob))

def generate_and_test_graphs(erdos_parameters_range, protection_range, 
        graph_generations = 1, filename = None):
    for (prob, nodes) in erdos_parameters_range:
        er_generator = erdos_renyi.ErdosRenyi(prob, nodes)
        graph_generation_info = "Erdos Renyi, p = %s, n = %s" % (prob, nodes)
        print graph_generation_info
        result_history = result_keeper.ResultKeeper(er_generator,
                ["Protection", "Probability", "Standard Dev", "Network Effect"], filename)
        result_history.add_extra_information(graph_generation_info)
        for i in xrange(graph_generations):
            current_graph = graph.Graph(er_generator.draw_adjacency_matrix())

            print "Computing Graph %s" % (i)
            compute_average_probability(current_graph, protection_range, result_history)

        result_history.print_averages_grouped_by(0)

if __name__ == '__main__':
    erdos_parameters_range = [(0.05, 100)]
    protection_range = [float(i)/100 for i in xrange(5, 100, 5)]
    output_filename = 'output'

    generate_and_test_graphs(erdos_parameters_range, protection_range, 100, output_filename)
