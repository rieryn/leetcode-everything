class Solution:
    def calculate(self, s: str) -> int:
        stack, current = [], 0

        for c in '(' + s + ')':
            
            if c.isdigit():
                current = 10 * current + int(c)
            elif c == '(':
                stack += [0, '+']
                current = 0
            elif c != ' ':
                operator, previous = stack.pop(), stack.pop()
                current = previous + (current if operator == '+' else -current)
                
                if c == ')': continue
                stack += [current, c]
                current = 0
            print(stack)
            print(current)
        return current