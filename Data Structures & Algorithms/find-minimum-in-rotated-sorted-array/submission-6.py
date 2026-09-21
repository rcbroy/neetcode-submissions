class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        i, j = 1, len(nums)-1
        while i <= j:
            m = (i+j) // 2
            if nums[m] < minimum:
                minimum = nums[m]
                j = m-1
            else:
                i = m+1
        return minimum