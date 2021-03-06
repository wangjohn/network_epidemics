import infection
import graph
import erdos_renyi
import result_keeper

class Settings:
    def __init__(self, attack, cure):
        self.erdos_parameters_range = [(0.05, 100)]

        self.pref_attachment_parameters = [(5,100)]


        self.num_trials_per_protection = 10
        self.num_graphs = 1

        self.protection_range = [float(i)/100 for i in xrange(0, 100, 20)]
        self.protection_string = "{:15s} {:15s} {:15s} {:15s}"
        self.headers = ["Protection", "Probability", "Standard Dev", "Network Effect"]

        self.attack_probability = attack
        self.cure_probability = cure

        self.filename = 'erdos_renyi_dynamic_hiv'

        # Mechanism defaults
        self.infection_mechanism = 'dynamic'
        self.protection_mechanism = 'dynamic'

def compute_average_probability(settings, graph, result_history, num_trials = 100):
    print settings.protection_string.format(*settings.headers)
    for q in settings.protection_range:
        protection_list = [q for i in xrange(graph.num_nodes)]
        compute_probabilities_object = infection.ComputeInfectionProbabilities(
                graph, protection_list, 0,
                infection_mechanism = settings.infection_mechanism,
                protection_mechanism = settings.protection_mechanism,
                attack_probability = settings.attack_probability,
                cure_probability = settings.cure_probability)

        prob, std = compute_probabilities_object.monte_carlo_compute_summary(settings.num_trials_per_protection)
        result_history.append([q, prob, std, 1-q-prob], graph)
        print settings.protection_string.format(str(q), str(prob), str(std), str(1 - q - prob))

def generate_and_test_graphs(settings):
    for (prob, nodes) in settings.erdos_parameters_range:
        graph_generator = erdos_renyi.ErdosRenyi(prob, nodes)
        result_history = result_keeper.ResultKeeper(settings, graph_generator, settings.headers, settings.filename)

        graph_generation_info = "Preferential Attachment, k = %s, n = %s" % (prob, nodes)
        result_history.add_extra_information(graph_generation_info)
        print graph_generation_info

        for i in xrange(settings.num_graphs):
            current_graph = graph.Graph(graph_generator.draw_adjacency_matrix())

            print "Computing Graph %s" % (i)
            compute_average_probability(settings, current_graph, result_history)

        result_history.print_averages_grouped_by(0)

if __name__ == '__main__':
    for attack in [0.05]:
        for cure in [0.1, 0.3, 0.5, 0.7]:
            settings = Settings(attack,cure)
            generate_and_test_graphs(settings)
