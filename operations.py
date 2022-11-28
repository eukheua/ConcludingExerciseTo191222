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
    def __init__(self, symbol, order_in_operations, position,operation_func):
        self.symbol = is_valid_symbol(symbol)
        self.order_in_operations = is_valid_symbol_order_in_operations(order_in_operations)
        self.position = position
        self.operation_func = operation_func

class Add:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        return self.op1 + op2


class Subtract:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        return self.op1 - op2


class Multiply:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        return self.op1 * op2


class Divide:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        return self.op1 / op2


class Exponent:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        return pow(self.op1,  op2)

class Modulu:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        return self.op1 % op2

class Maximum:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        if self.op1>op2:
            return self.op1
        else:
            return op2
class Minimum:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        if self.op1<op2:
            return self.op1
        else:
            return op2
class Average:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self, op2):
        return (self.op1 + op2)/2

class Negation:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self):
        return -self.op1

class Factorial:
    def __init__(self, op1):
        self.op1 = op1

    def apply(self):
        return fac(self.op1)



class NoOp:
    def apply(self, __op):
        return __op

















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
