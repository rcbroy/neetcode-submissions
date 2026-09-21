class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        i, j = 1, max(piles)
        rate = j
        while i <= j:
            m = (i+j) // 2
            hours = 0
            for p in piles:
                hours += (p // m)
                if (p % m) != 0:
                    hours += 1
            if hours <= h:
                rate = min(rate, m)
                j = m-1
            else:
                i = m+1
        return rate