class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        def backtrack(sofar, i):
            if i == len(nums):
                if sum(sofar) == target:
                    sol.append(sofar.copy())
                return
            if sum(sofar) > target:
                return
            sofar.append(nums[i])
            backtrack(sofar, i)
            sofar.pop()
            backtrack(sofar, i+1)
        backtrack([], 0)
        return sol