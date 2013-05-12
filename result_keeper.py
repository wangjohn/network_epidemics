import collections

class ResultKeeper:
    def __init__(self, graph_generator, headers = None):
        self.graph_generator = graph_generator
        self.headers = headers
        self.results = []

    def row_headers(self, headers):
        self.headers = headers

    def append(self, result_list):
        self.results.append(result_list)

    def averages_grouped_by(self, group):
        grouped_results = collections.defaultdict(list)
        for result in self.results:
            grouped_results[result[group]].append(result)

        averages = {}
        for group_key, result_list in grouped_results.iteritems():
            averages[group_key] = self.average_list_elements(result_list, len(self.headers))

        return averages

    def print_averages_grouped_by(self, group, filename = None):
        self.print_out(("{:15s} " * len(self.headers)).format(self.headers), filename)
        format_string = "{:15f} " * len(self.headers)
        for group_key, summary in self.averages_grouped_by(group).iteritems():
            string = format_string.format(*summary)
            self.print_out(string, filename)

    def print_out(self, string, filename):
        if filename:
            with open(filename, 'a') as f:
                f.write(string)
        print string

    def average_list_elements(self, result_list, result_size):
        averages = []
        for i in xrange(result_size):
            column_average = sum([result[i] for result in result_list]) * 1.0 / len(result_list)
            averages.append(column_average)
        return averages
