class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t in ops:
                right, left = stack.pop(), stack.pop()
                stack.append(str(int(eval(left+t+right))))
            else:
                stack.append(t)
        return int(stack.pop())