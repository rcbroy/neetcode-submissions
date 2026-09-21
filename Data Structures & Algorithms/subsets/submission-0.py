class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def helper(sofar, i):
            # print(i, nums[i], sofar, len(nums))
            if i == len(nums):
                sol.append(sofar.copy())
                return
            sofar += [nums[i]]
            helper(sofar, i+1)
            sofar.pop()
            helper(sofar, i+1)
        helper([], 0)
        return sol