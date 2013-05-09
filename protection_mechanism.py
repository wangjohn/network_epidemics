

class ProtectionMechanism:
    def __init__(self, infection_object):
        self.infection_object = infection_object
        self.cost_function = infection_object.cost_function

    def next_iteration(self):
        raise "Not Implemented"
