class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in "({[":
                stack.append(p)
            elif not stack:
                return False
            elif p == ')':
                if stack.pop() != '(':
                    return False
            elif p == '}':
                if stack.pop() != '{':
                    return False
            elif p == ']':
                if stack.pop() != '[':
                    return False
            else:
                return false
        return len(stack) == 0