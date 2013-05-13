import collections

class ResultKeeper:
    def __init__(self, graph_generator, headers = None, filename = None):
        self.graph_generator = graph_generator
        self.headers = headers
        self.results = []
        self.graphs_counter = collections.Counter()
        self.filename = filename
        self.extra_information = []

    def row_headers(self, headers):
        self.headers = headers

    def append(self, result_list, graph = None):
        self.results.append(result_list)
        self.graphs_counter[graph] += 1

    def add_extra_information(self, info):
        self.extra_information.append(info)

    def averages_grouped_by(self, group):
        grouped_results = collections.defaultdict(list)
        for result in self.results:
            grouped_results[result[group]].append(result)

        averages = {}
        for group_key, result_list in grouped_results.iteritems():
            averages[group_key] = self.average_list_elements(result_list, len(self.headers))

        return averages

    def print_averages_grouped_by(self, group):
        grouped_averages = self.averages_grouped_by(group)
        for info in self.extra_information:
            self.print_out(info)
        self.print_out("Total Number of Trials: %s" % len(self.results))
        self.print_out("Total Number of Groups: %s" % len(grouped_averages))
        self.print_out("Total Number of Graphs: %s" % len(self.graphs_counter))

        self.print_out(("{:15s} " * len(self.headers)).format(*self.headers))
        format_string = "{:15f} " * len(self.headers)
        for group_key, summary in grouped_averages.iteritems():
            self.print_out(format_string.format(*summary))

    def print_out(self, string):
        if self.filename:
            with open(self.filename, 'a') as f:
                f.write(string + "\n")
        print string

    def average_list_elements(self, result_list, result_size):
        averages = []
        for i in xrange(result_size):
            column_average = sum([result[i] for result in result_list]) * 1.0 / len(result_list)
            averages.append(column_average)
        return averages
