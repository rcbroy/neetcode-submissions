class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, j = stack.pop()
                ans.append((j, i-j))
            stack.append((t, i))
        while stack:
            temp, j = stack.pop()
            ans.append((j, 0))
        ans = sorted(ans, key=lambda x: x[0])
        return [y for (x,y) in ans]