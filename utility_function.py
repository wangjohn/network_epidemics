
# Utility function class. Default uses a polynomial cost function using the
# default of the PolynomialCostFunction class.
class UtilityFunction:
    def __init__(self, cost_function = None, uninfected_value = 1):
        self.uninfected_value = uninfected_value
        self.cost_function = cost_function

        if not self.cost_function:
            self.cost_function = PolynomialCostFunction()

    def calculate_utility(self, infection_probability, protection):
        cost = self.cost_function.calculate_cost(protection)
        return self.uninfected_value * infection_probability - cost

# An abstract class for the cost function. All cost functions should implement
# this base class, and should redefine the +calculate_cost+ method.
class CostFunction:
    def __init__(self, function_type = "polynomial"):
        self.function_type = function_type

    def calculate_cost(self, protection):
        raise "Not implemented"

# Polynomial cost function. The default cost function is just c(q) = q^2.
class PolynomialCostFunction(CostFunction):
    def __init__(self, function_type = "polynomial"):
        super(PolynomialCostFunction, self).__init__(function_type)
        self.coefficients = [0, 0, 0.5]

    def set_coefficients(self, coefficients):
        self.coefficients = coefficients

    def calculate_cost(self, protection):
        return sum([self.coefficients[i] * (protection ** i) for i in xrange(len(self.coefficients))])

