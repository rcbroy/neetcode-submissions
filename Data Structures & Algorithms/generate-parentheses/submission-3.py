class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def adder(text, opening, closing):
            if not closing:
                ans.append(text)
            if opening < closing:
                right = adder(text + ')', opening, closing-1)
            if opening:
                left = adder(text + '(', opening-1, closing)
        adder("", n, n)
        return ans