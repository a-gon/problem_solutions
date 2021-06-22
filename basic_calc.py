import operator

class Calculator:
    def __init__(self):
        self.ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.floordiv
        }
    def calculate(self, s: str) -> int:
        print(s)
        if s.strip().isdigit():
            return int(s)
        for c in self.ops.keys():
            left, op, right = s.partition(c)
            if op in self.ops:
                return self.ops[op](self.calculate(left), self.calculate(right))


calc = Calculator()
print(calc.ops['-'](0, 1))
exit()

expressions = ["3+2*2", " 3/2 ", " 3+5 / 2 ", "1-1-1-1-1"]
expected = [7, 1, 5, -4]
for i in range(len(expressions)):
    assert calc.calculate(expressions[i]) == expected[i], f'Expression {i+1} is incorrect: {calc.calculate(expressions[i])} '