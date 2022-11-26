from utils import *
from operations import *
from test import *
from config import *
from input import *


def evaluate_expression(expression):
    validate_brackets(expression)
    numbers_list = converting_string_nums_to_nums_list(expression)
    operations_list = converting_string_operators_to_operators_list(expression)
    return calculate(None, numbers_list, 0, len(numbers_list)-1, operations_list, 0, len(operations_list) - 1)


def calculate(replacing_number, numbers_list, numbers_list_start_index, numbers_list_end_index, operations_list,
              operations_list_start_index, operations_list_end_index):
    print("here")
    if numbers_list_start_index == numbers_list_end_index:
        if replacing_number is not None:
            return replacing_number
        # if only one number
        else:
            return numbers_list[numbers_list_start_index]
        # passed last operation
    elif operations_list_start_index > operations_list_end_index:
        return replacing_number
    operation = operations_list[operations_list_start_index]
    if replacing_number is None:
        number = numbers_list[numbers_list_start_index]
    else:
        number = replacing_number
    if operation == open_bracket:
        result = handle_bracket_operation(numbers_list, numbers_list_start_index, numbers_list_end_index,
                                          operations_list, operations_list_start_index, operations_list_end_index,
                                          operation)
    elif operation == factorial_sign:
        factorial = Factorial(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            factorial)
    elif operation == negation_sign:
        negation = Negation(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            negation)
    elif operation == modulo_sign:
        modulo = Modulu(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            modulo)
    elif operation == average_sign:
        average = Average(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            average)
    elif operation == minimum_sign:
        minimum = Minimum(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            minimum)
    elif operation == maximum_sign:
        maximum = Maximum(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            maximum)
    elif operation == exponent_sign:
        exponent = Exponent(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            exponent)
    elif operation == multiplication_sign:
        multiplication = Multiply(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            multiplication)
    elif operation == division_sign:
        division = Divide(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            division)
    elif operation == addition_sign:
        addition = Add(number)
        result = handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index,
                                                            numbers_list_end_index, operations_list,
                                                            operations_list_start_index, operations_list_end_index,
                                                            addition)
    elif operation == subtraction_sign:
        subtraction = Subtract(number)
        result = handle_subtraction(numbers_list, numbers_list_start_index,
                                    numbers_list_end_index, operations_list,
                                    operations_list_start_index, operations_list_end_index,
                                    subtraction)
    else:
        raise RuntimeError("operation " + operation + " unknown")
    return result


def handle_bracket_operation(numbers_list, numbers_list_start_index, numbers_list_end_index, operations_list,
                             operations_list_start_index, operations_list_end_index, operation):
    index_of_closing_bracket = find_index_of_closing_bracket(operations_list, operations_list_start_index)
    number_of_numbers_in_brackets = find_numbers_between_operators(operations_list, operations_list_start_index,
                                                                   operations_list_end_index)
    result_of_brackets = calculate(None, numbers_list, numbers_list_start_index, number_of_numbers_in_brackets,
                                   operations_list, operations_list_start_index + 1, index_of_closing_bracket - 1)
    return calculate(result_of_brackets, numbers_list, number_of_numbers_in_brackets, numbers_list_end_index,
                     operations_list,
                     index_of_closing_bracket + 1, operations_list_end_index)


def handle_operation_with_potential_precedence(numbers_list, numbers_list_start_index, numbers_list_end_index,
                                               operations_list,
                                               operations_list_start_index, operations_list_end_index, operation):
    if operations_list_start_index != operations_list_end_index and operations_list[
        operations_list_start_index + 1] == open_bracket:
        return handle_bracket_operation(numbers_list, numbers_list_start_index + 1, numbers_list_end_index,
                                        operations_list,
                                        operations_list_start_index + 1, operations_list_end_index, operation)
    else:
        number = operation.apply((numbers_list[numbers_list_start_index + 1]))
        return calculate(number, numbers_list, numbers_list_start_index + 1, numbers_list_end_index, operations_list,
                         operations_list_start_index + 1, operations_list_end_index)


def handle_subtraction(numbers_list, numbers_list_start_index, numbers_list_end_index, operations_list,
                       operations_list_start_index, operations_list_end_index, subtract):
    if operations_list_end_index - operations_list_start_index >= 1 and (
            operations_list[operations_list_start_index + 1] == addition_sign or operations_list[
        operations_list_start_index + 1] == "-"):
        number = subtract.apply(numbers_list[numbers_list_start_index + 1])
        result = calculate(number, numbers_list, numbers_list_start_index + 1, numbers_list_end_index, operations_list,
                           operations_list_start_index + 1, operations_list_end_index)
    elif operations_list_end_index - operations_list_start_index == 0:
        result = subtract.apply(numbers_list[numbers_list_start_index + 1])

    else:
        index_of_next_addition_or_subtraction = find_operation_up_to_next_add_or_sub(operations_list,
                                                                                     operations_list_start_index + 1,
                                                                                     operations_list_end_index)
        index_of_last_num_between_operators = find_numbers_between_operators(operations_list, 1,
                                                                             index_of_next_addition_or_subtraction) + numbers_list_start_index
        number = subtract.apply(
            calculate(None, numbers_list, numbers_list_start_index + 1, index_of_last_num_between_operators,
                      operations_list, operations_list_start_index + 1, index_of_next_addition_or_subtraction))
        result = calculate(number, numbers_list, index_of_last_num_between_operators, numbers_list_end_index,
                           operations_list, index_of_next_addition_or_subtraction + 1, operations_list_end_index)
    return result
