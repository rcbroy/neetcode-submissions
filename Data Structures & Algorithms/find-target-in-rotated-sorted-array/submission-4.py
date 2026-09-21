class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 1, len(nums) - 1
        min_index = 0
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] < nums[min_index]:
                min_index = mid
                j = mid - 1
            else:
                i = mid + 1
        print(min_index)
        i, j = 0, len(nums) - 1
        if target <= nums[j]:
            i = min_index
        else:
            j = min_index - 1
        while i <= j:
            mid = (i+j) // 2
            if target < nums[mid]:
                j = mid-1
            elif target > nums[mid]:
                i = mid+1
            else:
                return mid
        return -1
