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
            averages[group_key] = average_list_elements(result_list, len(self.headers))

        return averages

    def print_averages_grouped_by(self, group):
        print self.headers
        format_string = "{:15s} " * len(self.headers)
        for group_key, summary in self.averages_grouped_by(group):
            print format_string.format(*current_list)

    def average_list_elements(self, result_list, result_size):
        averages = []
        for i in xrange(result_size):
            column_average = sum([result[i] for result in result_list]) * 1.0 / len(result_list)
            averages.append(column_average)
        return averages
