class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        group = []
        def backtrack(opening, closing):
            if closing == n:
                ans.append("".join(group))
                return
            if opening > closing and closing < n:
                group.append(')')
                backtrack(opening, closing+1)
                group.pop()
            if opening < n:
                group.append('(')
                backtrack(opening+1, closing)
                group.pop()
        backtrack(0,0)
        return ans