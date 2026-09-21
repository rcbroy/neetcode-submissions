class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        def backtrack(t, i):
            if i == len(nums) or t < 0:
                return
            elif t == 0:
                ans.append(temp.copy())
            else:
                nn = nums[i]
                temp.append(nn)
                backtrack(t-nn, i)
                temp.pop()
                backtrack(t, i+1)
        backtrack(target, 0)
        return ans