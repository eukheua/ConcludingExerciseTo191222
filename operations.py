import math


def is_valid_symbol(symbol):
    if symbol not in "+-*/^%$&@~!":
        raise ValueError("Not valid operator")
    return symbol


def is_valid_symbol_order_in_operations(order_in_operations):
    if order_in_operations not in range(1, 7):
        raise ValueError("Not valid order_in_operations")
    return order_in_operations


def is_valid_position(position):
    if position != "left" and position != "right" and position != "middle":
        raise ValueError("Not valid position")
    return position


class Operator(object):
    def __init__(self, symbol, order_in_operations, position):
        self.symbol = is_valid_symbol(symbol)
        self.order_in_operations = is_valid_symbol_order_in_operations(order_in_operations)
        self.position = position


def add(op1, op2):
    return op1 + op2


def sub(op1, op2):
    return op1 - op2


def mul(op1, op2):
    return op1 * op2


def div(op1, op2):
    return op1 / op2


def power(op1, op2):
    return math.pow(op1, op2)


def mod(op1, op2):
    return op1 % op2


def maximum(op1, op2):
    if op1 > op2:
        return op1
    else:
        return op2


def minimum(op1, op2):
    if op1 < op2:
        return op1
    else:
        return op2


def avg(op1, op2):
    return (op1 + op2) / 2


def neg(op):
    return -op


def fac(op):
    if op == 1 or op == 0:
        return 1
    return fac(op-1) * op
