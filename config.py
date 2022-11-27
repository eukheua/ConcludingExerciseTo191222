OPERATION_ORDER_DICT = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
OPERATORS_STRING = "+-*/^%$&@~!"
SUPPORTED_BRACKETS = "()"
DIGITS = "0123456789"

open_bracket = '('
closed_bracket = ')'
addition_sign = '+'
subtraction_sign = '-'
multiplication_sign = '*'
division_sign = '/'
exponent_sign = '^'
modulo_sign = '%'
maximum_sign = '$'
minimum_sign = '&'
average_sign = '@'
negation_sign = '~'
factorial_sign = '!'

supported_operations = {addition_sign, subtraction_sign, multiplication_sign, division_sign, exponent_sign, modulo_sign,
                        maximum_sign, minimum_sign, average_sign, negation_sign, factorial_sign}

#  includes all supported characters excluding numbers
supported_operators = supported_operations.union(open_bracket, closed_bracket)

supported_operators_plus = supported_operations.union(open_bracket)
