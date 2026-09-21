class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(s, e):
            if s <= e:
                mid = (e+s) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binarySearch(mid+1, e)
                else:
                    return binarySearch(s, mid-1)
            else:
                return -1
        return binarySearch(0, len(nums)-1)