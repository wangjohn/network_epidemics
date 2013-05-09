
class UtilityFunction:
    def __init__(self, cost_function, uninfected_value = 1):
        self.cost_function = cost_function
        self.uninfected_value = uninfected_value

# Polynomial cost function. The default cost function is just c(q) = q^2.
class CostFunction:
    def __init__(self, function_type = "polynomial"):
        self.function_type = function_type
        self.coefficients = [0, 0, 0.5]

    def set_coefficients(self, coefficients):
        self.coefficients = coefficients

    def calculate_cost(self, protection):
        return sum([self.coefficients[i] * (protection ** i) for i in xrange(len(self.coefficients))])

