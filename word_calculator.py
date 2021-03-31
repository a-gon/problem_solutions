import operator

class Calculator:
    def __init__(self):
        self.num_dict = {'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9,
                'ten': 10
        }
        self.op_dict = {'plus': '+',
                'minus': '-',
                'times': '*',
                'divided': '/'
        }


    def parse(self, input):
        line = input.split(' ')
        # expression = []
        expression = ''
        for i in line:
            if i in self.num_dict:
                # expression.append(self.num_dict[i])
                expression += str(self.num_dict[i])
            elif i in self.op_dict:
                # expression.append(self.op_dict[i])
                expression += self.op_dict[i]
        print(expression)
        return expression

    def calculate(self, expression):
        if expression.isdigit():
            return float(expression)
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
        }
        for c in ops.keys():
            left, op, right = expression.partition(c)
            if op in ops:
                return ops[op](self.calculate(left), self.calculate(right))



input = 'two times three plus ten divided by five minus one'
calc = Calculator()
print(f'{input} \nEvaluates to {calc.calculate(calc.parse(input))}')