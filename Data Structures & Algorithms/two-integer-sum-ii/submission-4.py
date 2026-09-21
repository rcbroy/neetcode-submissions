class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bsearch(t, index):
            j = len(numbers) - 1
            while index <= j:
                mid = (index + j) // 2
                if t == numbers[mid]:
                    return mid
                elif t < numbers[mid]:
                    j = mid-1
                else:
                    index = mid + 1
            return -1
        for i, n in enumerate(numbers):
            maybe = bsearch(target-n, i+1)
            if maybe > -1:
                return [i+1, maybe+1]
            