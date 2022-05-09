class Parser(object):
    def __init__(self):
        pass

    def parse(self, expression):
        a, op, b = tuple(expression.split(' '))
        return float(a), float(b), op


class Core(object):
    def __init__(self):
        self._parser = Parser()
        self._functions = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '^': lambda a, b: a ** b
        }

    @staticmethod
    def check_zero_division(expression):
        try:
            action = expression.split((' '))
            if action[1] == '/' and action[2] == '0':
                raise ZeroDivisionError
            else:
                return True
        except ZeroDivisionError as eror:
            print("Can't divizion zero", eror)

    def check_value(self, expression):
        count = 0
        try:
            action = expression.split((' '))
            for operand in self._functions:
                if operand == action[1]:
                    count = 1
                    break
            if count == 0:
                raise ValueError
            elif len(action) < 3:
                raise ValueError
            else:
                return True
        except ValueError as e:
            print('Need 2 numb and operator, Example: 24 * 16', e)

    def calculate(self, expression):
        if self.check_value(expression):
            if self.check_zero_division(expression):
                a, b, op = self._parser.parse(expression)
                result = self._functions.get(op)(a, b)
                return result


class Interface(object):
    def __init__(self):
        self._core = Core()

    def run_calculator(self):
        while True:
            print('Enter your expression: ')
            expression = input()
            result = self._core.calculate(expression)
            print("Your result: {}".format(result))
            print('_' * 10)


if __name__ == "__main__":
    calculator = Interface()
    calculator.run_calculator()
