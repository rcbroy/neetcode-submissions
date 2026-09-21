class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(start, end, target):
            if end <= start:
                return -1
            k = (start+end) // 2
            if numbers[k] == target:
                return k
            elif numbers[k] > target:
                return binary_search(start, k, target)
            else:
                return binary_search(k+1, end, target)
        for i, n in enumerate(numbers):
            j = binary_search(i+1, len(numbers), target-n)
            if j != -1:
                return [i+1, j+1]
        return [-1, -1]