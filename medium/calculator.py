def calculate(s):
    stack = []
    cur_num = 0
    cur_op = '+'
    for i in range(len(s)):
        if s[i].isdigit():
            cur_num = cur_num * 10 + int(s[i])
        if s[i] in '+-*/' or i == len(s) - 1:
            if cur_op == '+':
                stack.append(cur_num)
            elif cur_op == '-':
                stack.append(-cur_num)
            elif cur_op == '*':
                stack.append(stack.pop() * cur_num)
            elif cur_op == '/':
                stack.append(int(stack.pop() / cur_num))
            cur_op = s[i]
            cur_num = 0
    return sum(stack)

print(calculate('3+2 *2'))
print(calculate('003+2 *0'))

