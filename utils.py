from config import *


def find_index_of_closing_bracket():
    pass


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


def converting_string_operators_to_operators_list(expression):
    operators_list = []
    for char in expression:
        if char in OPERATORS_STRING:
            operators_list.append(char)
        elif char.isdigit() is False:
            raise RuntimeError("Unsupported symbol " + char)
    return operators_list

def validate_brackets(expression):
    stack = []
    for char in expression:
        if char == open_bracket:
            stack.append(char)
        elif char == closed_bracket:
            if len(stack) == 0:
                return False
            stack.pop()
        elif char.isdigit() is False and char not in OPERATORS_STRING:
            raise RuntimeError("Unsupported symbol " + char)
    if len(stack) == 0:
        return True
    return False
