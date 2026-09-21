class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l+r)
                elif t == '-':
                    stack.append(l-r)
                elif t == '*':
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))
            print(stack)
        return stack.pop()