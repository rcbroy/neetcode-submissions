class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '})]':
                if not stack:
                    return False
                s = stack[-1]
                if p == '}' and s != '{' or p == ')' and s != '(' or p == ']' and s != '[':
                    return False
                stack.pop()
            else:
                stack.append(p)
        return not stack