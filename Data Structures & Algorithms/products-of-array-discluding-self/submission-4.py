class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        result = []
        for n in nums:
            result.append(p)
            p *= n
        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * p
            p *= nums[i]
        return result