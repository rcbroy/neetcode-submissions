class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        ans = []
        for n in nums:
            ans.append(p)
            p *= n
        p = 1
        for i in range(len(nums)-1, -1, -1):
            print(i)
            ans[i] *= p
            p *= nums[i]
        return ans