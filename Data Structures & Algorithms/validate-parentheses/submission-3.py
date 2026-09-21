class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complements = {'(': ')', '{': '}', '[': ']'}
        for p in s:
            if p in "({[":
                stack.append(p)
            elif not stack:
                return False
            elif complements[stack.pop()] != p:
                return False
        return len(stack) == 0