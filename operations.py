def main():
    operations_order_dict = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}

    class Operator(object):
        def __init__(self, symbol, order_in_operations, position):
            self.symbol = symbol
            self.order_in_operations = order_in_operations
            self.position = position

        def is_valid_symbol(self, symbol):
            if symbol not in "+-*/^%$&@~!":
                raise ValueError("Not valid operator")
            return symbol
        def is_valid_symbol_order_in_operations(self, order_in_operations):
            if order_in_operations not in range(1,7):
                raise ValueError("Not valid order_in_operations")
            return order_in_operations
        def is_valid_position(self, position):
            if position != "left" and position != "right" and position != "middle" :
                raise ValueError("Not valid position")
            return position

        def get_first_name(self):
            return self.first_name

        def get_last_name(self):
            return self.last_name

        def get_age(self):
            return self.age

        def set_first_name(self, first_name):
            self.first_name = first_name

        def set_last_name(self, last_name):
            self.last_name = last_name

        def set_age(self, age):
            self.age = age

if __name__ == "__main__":
    main()
