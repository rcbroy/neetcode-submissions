class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
                zero_idx = i
            else:
                product *= n
        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            l = [0] * len(nums)
            l[zero_idx] = product
            return l
        l = [product] * len(nums)
        for i, n in enumerate(nums):
            l[i] = l[i]//n
        return l