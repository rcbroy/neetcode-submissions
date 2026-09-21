class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        temp = []
        def backtrack(n):
            if n == len(nums):
                return
            temp.append(nums[n])
            ans.append(temp.copy())
            backtrack(n+1)
            temp.pop()
            backtrack(n+1)
        backtrack(0)
        return ans