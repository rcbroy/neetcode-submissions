from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = max(piles)
        left_k, right_k = 1, min_k - 1
        def calcHours(k):
            h = 0
            for p in piles:
                h += ceil(p/k)
            return h
        while left_k <= right_k:
            mk = (left_k + right_k) // 2
            hours = calcHours(mk)
            if hours > h:
                left_k = mk + 1
            else:
                right_k = mk - 1
                min_k = min(min_k, mk)
        return min_k