from config import *


def find_index_of_closing_bracket(operations_list, operations_list_start_index):
    stack = []
    current_index = operations_list_start_index
    index_to_return = current_index
    for i in range(operations_list_start_index, len(operations_list)):
        operation = operations_list[i]
        if len(stack) == 0 and index_to_return != operations_list_start_index:
            return index_to_return
        if operation == open_bracket:
            stack.append(operation)
        elif operation == closed_bracket:
            stack.pop()
            index_to_return = current_index
        current_index += 1

    return index_to_return


def find_numbers_between_operators(operations_list, operations_list_start_index, operations_list_end_index):
    quantity_of_numbers_between_operators = 0
    if operations_list[operations_list_start_index] in supported_operations:
        quantity_of_numbers_between_operators += 1
    for i in range(operations_list_start_index, operations_list_end_index + 1):
        operation = operations_list[i]
        # if now operations between
        if operation in supported_operations and i + 1 == operations_list_end_index + 1:
            return quantity_of_numbers_between_operators + 1
        elif i + 1 == len(operations_list):
            break
        next_operation = operations_list[i + 1]

        if operation == negation_sign or operation == factorial_sign:
            continue
        elif operation == open_bracket and next_operation in supported_operations:
            quantity_of_numbers_between_operators += 1
        elif operation in supported_operations and next_operation == closed_bracket:
            quantity_of_numbers_between_operators += 1
        elif operation in supported_operations and next_operation in supported_operations:
            quantity_of_numbers_between_operators += 1
    return quantity_of_numbers_between_operators


def find_operation_up_to_next_add_or_sub(operations_list, start_index, end_index):
    i = start_index
    while i <= end_index:
        if operations_list[i] == addition_sign or operations_list[i] == subtraction_sign:
            return i - 1
        if operations_list[i] == open_bracket:
            i = find_index_of_closing_bracket(operations_list, i) + 1
        else:
            i += 1
    return i - 1


def converting_string_nums_to_nums_list(expression):
    nums_list = []
    num_str = ""
    for char in expression:
        if char.isdigit() or char == ".":
            num_str += char
        else:
            if num_str != "":
                nums_list.append(float(num_str))
                num_str = ""
    if num_str != "":
        nums_list.append(float(num_str))
    return nums_list


def clean_spaces(expression):
    return "".join(expression.split(" "))


def convert_string_expression_to_list(expression):
    expression_list = []
    number = ""
    for char in expression:
        if char.isdigit() == True or char == ".":
            number += char
        else:
            if number != "":
                expression_list.append(float(number))
                number = ""
            if char in supported_operators:
                expression_list.append(char)
    if number != "":
        expression_list.append(float(number))
        number = ""
    return expression_list


def convert_infix_to_postfix(expression_list):
    stack = []
    postfix_expression_list = []
    for item in expression_list:
        if type(item) == float:
            postfix_expression_list.append(item)
        else:
            if item == closed_bracket:
                while stack[len(stack) - 1] != open_bracket:
                    postfix_expression_list += stack.pop()
                stack.pop()
            elif item == open_bracket:
                stack.append(item)
            else:
                if len(stack) != 0:
                    if stack[len(stack) - 1] != open_bracket:
                        while len(stack) != 0 and OPERATION_ORDER_DICT[stack[len(stack) - 1]] >= OPERATION_ORDER_DICT[item]:
                            postfix_expression_list.append(stack.pop())
                stack.append(item)
    while len(stack) != 0:
        postfix_expression_list.append(stack.pop())
    return postfix_expression_list


def converting_string_operators_to_operators_list(expression):
    operators_list = []
    for char in expression:
        if char in supported_operators:
            operators_list.append(char)
        elif char.isdigit() is False:
            raise RuntimeError("Unsupported symbol " + char)
    return operators_list


def validate_brackets(expression):
    stack = []
    index = 0
    index_of_opened = index
    not_balanced = False
    for char in expression:
        if char == open_bracket:
            stack.append(char)
            index_of_opened = index
        if char == closed_bracket:
            if len(stack) == 0:
                not_balanced = True
            stack.pop()
        index += 1
    if len(stack) == 0:
        return True
    else:
        not_balanced = True
    if not_balanced:
        message_of_bracket_imbalance = "Unbalanced bracket at \n" \
                                       + expression[:index_of_opened] + "  ->" + expression[index_of_opened] + "<-  " \
                                       + expression[index_of_opened + 1:len(expression)] \
                                       + "\n" + "index of bracket " + str(index_of_opened)
        raise RuntimeError(message_of_bracket_imbalance)


def parse_operators(o):
    r = []
    for i in o:
        if i == ' ':
            continue
        if i in supported_operators:
            r.append(i)
        elif not i.isdigit() and i != '.':
            raise RuntimeError('Unsupported symbol ' + i)

    return r
