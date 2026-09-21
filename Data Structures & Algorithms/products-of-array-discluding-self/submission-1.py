class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l < 2:
            return nums
        prefix = [1] * l
        postfix = [1] * l
        product = 1
        for i, n in enumerate(nums[1:]):
            product *= nums[i]
            prefix[i+1] = product
        product = 1
        for i in range(l-1, 0, -1):
            product *= nums[i]
            postfix[i-1] = product
        for i, n in enumerate(postfix):
            prefix[i] = prefix[i] * n
        return prefix