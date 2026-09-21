class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        temp = []
        def backtrack(i):
            if i == len(nums):
                return
            temp.append(nums[i])
            ans.append(temp.copy())
            backtrack(i+1)
            temp.pop()
            backtrack(i+1)
        backtrack(0)
        return ans