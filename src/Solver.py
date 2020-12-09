
class Solver:

    def apply(self, value1, value2, operator):
        if operator == '+':
            return value1 + value2
        if operator == '-':
            return value1 - value2
        if operator == '*':
            return value1 * value2
        if operator == '/':
            return value1 / value2
        raise SyntaxError('Wrong expression.')

    def binary_operation(self, value_stack, operator_stack):
        value2 = value_stack.pop()
        value1 = value_stack.pop()
        operator = operator_stack.pop()
        result = self.apply(value1, value2, operator)
        value_stack.append(result)

    def priority(self, x):
        if x == '*' or x == '/':
            return 2
        if x == '+' or x == '-':
            return 1
        return 0

    def solve(self, expression):
        value_stack = []
        operator_stack = []
        operators = '+-*/'

        if expression[0] == '+':
            expression = expression[1:]
        if expression[0] == '-':
            expression = '0' + expression
        expression = expression.replace('(-', '(0-')

        i = 0
        while (True):
            if i >= len(expression):
                while operator_stack:
                    operator = operator_stack.pop(0)
                    value1 = value_stack.pop(0)
                    value2 = value_stack.pop(0)
                    result = self.apply(value1, value2, operator)
                    value_stack.insert(0, result)
                if len(value_stack) != 1:
                    raise SyntaxError('Wrong expression.')
                return value_stack.pop()

            elif expression[i].isdigit():
                value = int(expression[i])
                i += 1
                while (i < len(expression) and expression[i].isdigit()):
                    value = value * 10 + int(expression[i])
                    i += 1
                value_stack.append(value)
                if len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] in '*/':
                    self.binary_operation(value_stack, operator_stack)
                i -= 1

            elif expression[i] in operators:
                if (len(operator_stack) >= 1 and self.priority(operator_stack[len(operator_stack) - 1]) >= self.priority(expression[i])):
                    self.binary_operation(value_stack, operator_stack)
                operator_stack.append(expression[i])

            elif expression[i] == '(':
                operator_stack.append('(')

            elif expression[i] == ')':
                while (operator_stack[len(operator_stack) - 1] != '('):
                    self.binary_operation(value_stack, operator_stack)
                operator_stack.pop()

            else:
                raise SyntaxError('Wrong expression.')
            i += 1