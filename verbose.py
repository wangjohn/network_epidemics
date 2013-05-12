
# Class for printing out objects and logging them.
class Verbose:
    def __init__(self, verbose = True):
        self.log = []
        self.verbose = verbose

    def p(self, *args):
        string = "".join([str(i) for i in args])
        self.log.append(string)
        print string

    def flush_log(self, filename):
        with open(filename, 'w') as f:
            for s in self.log:
                f.write(s)
