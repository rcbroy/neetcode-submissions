class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        if nums[i] <= nums[j]:
            return nums[i]
        while i < j:
            m = (i+1+j) // 2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m
        return nums[m]