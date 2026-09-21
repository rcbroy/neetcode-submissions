class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []
        def backtrack(opening, closing):
            if closing == 0:
                ans.append(''.join(temp))
                return
            if opening < closing:
                temp.append(')')
                backtrack(opening, closing-1)
                temp.pop()
            if opening > 0:
                temp.append('(')
                backtrack(opening-1, closing)
                temp.pop()
        backtrack(n, n)
        return ans

        # ans = []
        # group = []
        # def backtrack(opening, closing):
        #     if closing == n:
        #         ans.append("".join(group))
        #         return
        #     if opening > closing and closing < n:
        #         group.append(')')
        #         backtrack(opening, closing+1)
        #         group.pop()
        #     if opening < n:
        #         group.append('(')
        #         backtrack(opening+1, closing)
        #         group.pop()
        # backtrack(0,0)
        # return ans