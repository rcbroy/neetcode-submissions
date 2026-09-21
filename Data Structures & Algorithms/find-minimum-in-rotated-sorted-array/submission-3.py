class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        if nums[i] <= nums[j]:
            return nums[i]
        # if len(nums) == 1:
        #     return nums[0]
        while i <= j:
            m = (i+j) // 2
            # print(i, j, m)
            if nums[m] < nums[j]:
                j = m
            else:
                i = m+1
        return nums[m]