class Random_Function():
    def __init__(self, symbol, verbose = False, diagnostics = False):
        
            # Programmatic Information:
        self.symbol = symbol
        self.random_function = 0
        self.number_of_upper_functions = 0
        self.number_of_lower_functions = 0
        self.upper_function = None
        self.lower_function = None
        self.is_function_a_quotient = None
        
            # Debugging:
        self.verbose = verbose
        self.diagnostics = diagnostics
        self.diagnostic_report = ""
        
            # Probabilities
        self.PROBABILITY_OF_ONE_UPPER_FUNCTION = 0.93
        self.PROBABILITY_OF_TWO_UPPER_FUNCTIONS = 0.03
        self.PROBABILITY_OF_THREE_UPPER_FUNCTIONS = 0.02
        self.PROBABILITY_OF_FOUR_UPPER_FUNCTIONS = 0.01
        self.PROBABILITY_OF_FIVE_UPPER_FUNCTIONS = 0.01
        
        self.PROBABILITY_OF_ONE_LOWER_FUNCTION = 0.93
        self.PROBABILITY_OF_TWO_LOWER_FUNCTIONS = 0.03
        self.PROBABILITY_OF_THREE_LOWER_FUNCTIONS = 0.02
        self.PROBABILITY_OF_FOUR_LOWER_FUNCTIONS = 0.01
        self.PROBABILITY_OF_FIVE_LOWER_FUNCTIONS = 0.01
        
        self.PROBABILITY_OF_PRODUCT_OF_TWO_FUNCTIONS = 0.95
        self.PROBABILITY_OF_PRODUCT_OF_THREE_FUNCTIONS = 0.02
        self.PROBABILITY_OF_PRODUCT_OF_FOUR_FUNCTIONS = 0.02
        self.PROBABILITY_OF_PRODUCT_OF_FIVE_FUNCTIONS = 0.01
        
        self.PROBABILITY_OF_PRODUCT = 0.2
        
        self.PROBABILITY_OF_ARGUMENT_MANIPULATION = 0.75
        
            # References:
        self.LIST_OF_ELEMENTARY_FUNCTIONS = [
            "constant",
            "power",
            "polynomial",
            "square_root",
            "nth_root",
            "exponential",
            "logarithmic",
            "trigonometric",
            "hyperbolic",
            "inverse_trigonometric"
        ]
        
        self.PROBABILITY_OF_ELEMENTARY_FUNCTION = [
            0.04,
            0.12,
            0.43,
            0.05,
            0.01,
            0.08,
            0.08,
            0.15,
            0.02,
            0.02
        ]
        
        self.TYPES_OF_ARGUMENT_MANIPULATION = [
            "addition_or_subtraction_of_constant",
            "multiplication_of_constant",
            "inverse",
        ]

        self.LIST_OF_TRIGONOMETRIC_FUNCTIONS = [
            "sine",
            "cosine",
            "tangent",
            "secant",
            "cosecant",
            "cotangent"
        ]

        self.LIST_OF_INVERSE_TRIGONOMETRIC_FUNCTIONS = [
            "arcsine",
            "arccosine",
            "arctangent",
            "arcsecant",
            "arccosecant",
            "arccotangent"
        ]

        self.LIST_OF_HYPERBOLIC_TRIGONOMETRIC_FUNCTIONS = [
            "sineh",
            "cosineh",
            "tangenth",
            "secanth",
            "cosecanth",
            "cotangenth"
        ]

        self.LIST_OF_POSSIBLE_FUNCTIONAL_FORMS = [
            "rational",
            "product"
        ]
        self.resources = "# https://en.wikipedia.org/wiki/Elementary_function"
        
    def choose_if_function_is_quotient(self):
        if self.verbose:
            print("> Now choosing if the R(x) is a quotient function...")
        self.is_random_function_a_quotient = np.random.choice([True, False], p = [0.5, 0.5])
        if self.diagnostics:
            self.diagnostic_report += f"* Is the R(x) a quotient function? {self.is_random_function_a_quotient}.\n"
        if self.verbose:
            print(f"> Is the R(x) a quotient function? {self.is_random_function_a_quotient}.\n")
        return self
    
    def choose_number_of_upper_functions(self):
        if self.verbose:
            print("> Now choosing number of upper functions composing F(x)...")
        self.number_of_upper_functions = np.random.choice(
            [1, 2, 3, 4, 5], 
            p = [
                self.PROBABILITY_OF_ONE_UPPER_FUNCTION,
                self.PROBABILITY_OF_TWO_UPPER_FUNCTIONS, 
                self.PROBABILITY_OF_THREE_UPPER_FUNCTIONS,
                self.PROBABILITY_OF_FOUR_UPPER_FUNCTIONS,
                self.PROBABILITY_OF_FIVE_UPPER_FUNCTIONS
            ])
        if self.verbose:
            print(f"> Chose {self.number_of_upper_functions} upper functions composing F(x).")
        if self.diagnostics:
            self.diagnostic_report += f"* Chose {self.number_of_upper_functions} upper functions composing F(x).\n"
        return self
    
    def choose_number_of_lower_functions(self):
        if self.verbose:
            print("> Now choosing number of lower functions composing G(x)...")
        self.number_of_lower_functions = np.random.choice(
            [1, 2, 3, 4, 5], 
            p = [
                self.PROBABILITY_OF_ONE_LOWER_FUNCTION,
                self.PROBABILITY_OF_TWO_LOWER_FUNCTIONS, 
                self.PROBABILITY_OF_THREE_LOWER_FUNCTIONS,
                self.PROBABILITY_OF_FOUR_LOWER_FUNCTIONS,
                self.PROBABILITY_OF_FIVE_LOWER_FUNCTIONS
            ])
        if self.verbose:
            print(f"> Chose {self.number_of_lower_functions} lower functions composing G(x).")
        if self.diagnostics:
            self.diagnostic_report += f"* Chose {self.number_of_lower_functions} lower functions composing G(x).\n"
        return self
    
    def choose_function_will_have_product(self):
        if self.verbose:
            print("> Now choosing if the function is to be multiplied...")
        will_function_have_product = np.random.choice([True, False], p = [self.PROBABILITY_OF_PRODUCT, 1 - self.PROBABILITY_OF_PRODUCT])
        if self.verbose:
            print(f"> Will the function be multiplied? {will_function_have_product}.")
        return will_function_have_product
    
    def choose_number_of_functions_in_product(self):
        if self.verbose:
            print("> Now choosing the number of functions to multiply together...")
        number_of_functions = np.random.choice(
            [2, 3, 4, 5], 
            p = [
                self.PROBABILITY_OF_PRODUCT_OF_TWO_FUNCTIONS,
                self.PROBABILITY_OF_PRODUCT_OF_THREE_FUNCTIONS, 
                self.PROBABILITY_OF_PRODUCT_OF_FOUR_FUNCTIONS,
                self.PROBABILITY_OF_PRODUCT_OF_FIVE_FUNCTIONS
            ])
        if self.verbose:
            print(f"> Chose {number_of_functions} in product.")
        if self.diagnostics:
            self.diagnostic_report += f"* Chose {number_of_functions} in product.\n"
        return number_of_functions
    
    def choose_argument_manipulation_or_not(self):
        if self.verbose:
            print("> Now choosing to manipulate the argument of the function...")
        will_function_argument_manipulation = np.random.choice([True, False], p = [self.PROBABILITY_OF_ARGUMENT_MANIPULATION, 1 - self.PROBABILITY_OF_ARGUMENT_MANIPULATION])
        if self.verbose:
            print(f"> Will the function have an argument manipulation? {will_function_argument_manipulation}.")
        return will_function_argument_manipulation

    def select_random_elementary_function(self):
        chosen_function = np.random.choice(self.LIST_OF_ELEMENTARY_FUNCTIONS,
                                           p = self.PROBABILITY_OF_ELEMENTARY_FUNCTION)
        if self.verbose:
            print(f"> Chose random elementary function of {chosen_function} type.")
        return chosen_function
    
    def generate_random_elementary_function(self, function_type):
        """
            Generate a random elementary function of type:
            Constant
            Power
            Square Root
            Nth Root
            Exponential
            Logarithmic
            Trigonometric
            Inverse Trigonometric
            Hyperbolic
        """
        if self.verbose:
            print(f"> Using selected function type {function_type}")
        if function_type == "constant":
            elementary_function = (np.random.randint(10) + 1) * self.symbol
        elif function_type == "power":
            elementary_function = self.symbol ** (np.random.randint(10) + 1)
        elif function_type == "polynomial":
            elementary_function = self.generate_random_polynomial_of_degree_n(np.random.randint(5) + 1)
        elif function_type == "square_root":
            elementary_function = sympy.sqrt(self.symbol)
        elif function_type == "nth_root":
            elementary_function = sympy.root(self.symbol, np.random.randint(10) + 1)
        elif function_type == "exponential":
            elementary_function = sympy.exp(self.symbol)
        elif function_type == "logarithmic":
            elementary_function = sympy.log(self.symbol)
        elif function_type == "trigonometric":
            elementary_function = self.generate_random_trigonometric_function(self.select_random_trigonometric_function())
        elif function_type == "inverse_trigonometric":
            elementary_function = self.generate_random_inverse_trigonometric_function(self.select_random_inverse_trigonometric_function())
        elif function_type == "hyperbolic":
            elementary_function = self.generate_random_hyperbolic_trigonometric_function(select_random_hyperbolic_trigonometric_function())
        else:
            print('> There was an error.')
        if self.diagnostics:
            self.diagnostic_report += f"* Chose a random elementary function of {elementary_function} type.\n"
        return elementary_function

    def generate_random_constant_up_to_n(self, constant_upper_bound):
        return np.random.randint(constant_upper_bound) + 1
    
    def generate_random_polynomial_of_degree_n(self, degree):
        polynomial = 0
        for i in range(degree):
            polynomial += self.generate_random_constant_up_to_n(10) * (self.symbol**i)
        return sympy.simplify(polynomial)
    
    def select_random_trigonometric_function(self):
        chosen_function = self.LIST_OF_TRIGONOMETRIC_FUNCTIONS[np.random.randint(len(self.LIST_OF_TRIGONOMETRIC_FUNCTIONS))]
        if self.verbose:
            print(f"> Chose random trigonometric function: {chosen_function}")
        return chosen_function
    
    def generate_random_trigonometric_function(self, trigonometric_function_type):
        if self.verbose:
            print(f"> Using selected trigonometric function type {trigonometric_function_type}")
        if trigonometric_function_type == "sine":
            trigonometric_function = sympy.sin(self.symbol)
        if trigonometric_function_type == "cosine":
            trigonometric_function = sympy.cos(self.symbol)
        if trigonometric_function_type == "tangent":
            trigonometric_function = sympy.tan(self.symbol)
        if trigonometric_function_type == "secant":
            trigonometric_function = sympy.sec(self.symbol)
        if trigonometric_function_type == "cosecant":
            trigonometric_function = sympy.csc(self.symbol)
        if trigonometric_function_type == "cotangent":
            trigonometric_function = sympy.cot(self.symbol)
        return trigonometric_function
    
    def select_random_inverse_trigonometric_function(self):
        chosen_function = self.LIST_OF_INVERSE_TRIGONOMETRIC_FUNCTIONS[np.random.randint(len(self.LIST_OF_INVERSE_TRIGONOMETRIC_FUNCTIONS))]
        if self.verbose:
            print(f"> Chose a random inverse trigonometric function of {chosen_function} type.")
        return chosen_function
    
    def generate_random_inverse_trigonometric_function(self, trigonometric_function_type):
        if self.verbose:
            print(f"> Using selected inverse trigonometric function of {trigonometric_function_type} type.")
        if trigonometric_function_type == "arcsine":
            trigonometric_function = sympy.asin(self.symbol)
        if trigonometric_function_type == "arccosine":
            trigonometric_function = sympy.acos(self.symbol)
        if trigonometric_function_type == "arctangent":
            trigonometric_function = sympy.atan(self.symbol)
        if trigonometric_function_type == "arcsecant":
            trigonometric_function = sympy.asec(self.symbol)
        if trigonometric_function_type == "arccosecant":
            trigonometric_function = sympy.acsc(self.symbol)
        if trigonometric_function_type == "arccotangent":
            trigonometric_function = sympy.acot(self.symbol)
        return trigonometric_function
    
    def select_random_hyperbolic_trigonometric_function(self):
        chosen_function = self.LIST_OF_HYPERBOLIC_TRIGONOMETRIC_FUNCTIONS[np.random.randint(len(self.LIST_OF_HYPERBOLIC_TRIGONOMETRIC_FUNCTIONS))]
        if self.verbose:
            print(f"> Chose a random hyperbolic trigonometric function of {chosen_function} type.")
        return chosen_function
    
    def generate_random_hyperbolic_trigonometric_function(self, hyperbolic_function_type):
        if self.verbose:
            print(f"> Using selected hyperbolic function of {hyperbolic_function_type} type.")
        if hyperbolic_function_type == "sineh":
            trigonometric_function = sympy.sinh(self.symbol)
        if hyperbolic_function_type == "cosineh":
            trigonometric_function = sympy.cosh(self.symbol)
        if hyperbolic_function_type == "tangenth":
            trigonometric_function = sympy.tanh(self.symbol)
        if hyperbolic_function_type == "secanth":
            trigonometric_function = sympy.sech(self.symbol)
        if hyperbolic_function_type == "cosecanth":
            trigonometric_function = sympy.csch(self.symbol)
        if hyperbolic_function_type == "cotangenth":
            trigonometric_function = sympy.coth(self.symbol)
        return trigonometric_function
    
    def manipulate_argument(self, expression):
        manipulation = self.TYPES_OF_ARGUMENT_MANIPULATION[np.random.randint(len(self.TYPES_OF_ARGUMENT_MANIPULATION))]
        if self.verbose:
            print(f"> Chose argument manipulation of {manipulation} type.")
        if manipulation == "addition_or_subtraction_of_constant":
            return expression.subs(self.symbol, self.symbol + np.random.randint(-10, 11))
        elif manipulation == "multiplication_of_constant":
            return expression.subs(self.symbol, self.symbol * np.random.randint(-10, 11))
        elif manipulation == "inverse":
            return expression.subs(self.symbol, self.symbol**-1)
    
    def construct_numerator_function(self):
        if self.verbose:
            print("< -- Now constructing upper function F(x) -- >")
        upper_function = 0
        for i in range(self.number_of_upper_functions):
            if self.verbose:
                print(f"> Now constructing f_{i + 1}(x).")
            primary_function = self.generate_random_elementary_function(self.select_random_elementary_function())
            will_function_have_product = self.choose_function_will_have_product()
            will_function_have_argument_manipulation = self.choose_argument_manipulation_or_not()
            if self.verbose:
                print(f"> Will the function have a product? {will_function_have_product}")
                print(f"> Will the function have an argument manipulation? {will_function_have_argument_manipulation}")
            if will_function_have_argument_manipulation:
                primary_function = self.manipulate_argument(primary_function)
            if will_function_have_product:
                primary_function = (self.generate_random_elementary_function(self.select_random_elementary_function())) * primary_function 
            upper_function += primary_function
        self.upper_function = upper_function
        return self
    
    def construct_denominator_function(self):
        if self.verbose:
            print("< -- Now constructing lower function G(x) -- >")
        lower_function = 0
        for i in range(self.number_of_lower_functions):
            if self.verbose:
                print(f"> Now constructing g_{i + 1}(x).")
            primary_function = self.generate_random_elementary_function(self.select_random_elementary_function())
            will_function_have_product = self.choose_function_will_have_product()
            will_function_have_argument_manipulation = self.choose_argument_manipulation_or_not()
            if self.verbose:
                print(f"> Will the function have a product? {will_function_have_product}")
                print(f"> Will the function have an argument manipulation? {will_function_have_argument_manipulation}")
            if will_function_have_argument_manipulation:
                primary_function = self.manipulate_argument(primary_function)
            if will_function_have_product:
                primary_function = (self.generate_random_elementary_function(self.select_random_elementary_function())) * primary_function 
            lower_function += primary_function
        self.lower_function = lower_function
        return self

    def construct_random_function(self):
        self.choose_if_function_is_quotient()
        if self.verbose:
            print("< -- Now constructing R(x) -- >")
        self.choose_number_of_upper_functions()
        self.choose_number_of_lower_functions()
        if self.is_random_function_a_quotient:
            self.construct_numerator_function()
            self.construct_denominator_function()
            self.random_function = self.upper_function / self.lower_function
        else:
            self.construct_numerator_function()
            self.random_function = self.upper_function
        return self
        
    def summarize(self):
        print(self.diagnostic_report)
        return self
    
if __name__ == "__main__":
    try:
        import re as regular_expressions
        import os as operating_system
        import sys as system_specific
        import numpy as np
        import sympy
    except e as Exception:
        print(f"Error importing packages: {e}")
else:
    print(f"__name__ is not __main__. It is: {__name__}")
