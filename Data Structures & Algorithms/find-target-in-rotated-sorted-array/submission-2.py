class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i+j) // 2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m+1
        i, j = 0, len(nums) - 1
        if target <= nums[j]:
            i = m
        else:
            j = m
        while i <= j:
            m = (i+j) // 2
            print(i, j, m)
            if target > nums[m]:
                i = m+1
            elif target < nums[m]:
                j = m-1
            else:
                return m
        return -1