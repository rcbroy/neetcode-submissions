class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        def calculate_hours(rate):
            hours = 0
            for p in piles:
                hours += (p // rate)
                if p % rate != 0:
                    hours += 1
            return hours
        i = 1
        j = max(piles)
        while i <= j:
            m = (i+j) // 2
            hours = calculate_hours(m)
            if hours <= h:
                if m == 1:
                    return m
                if calculate_hours(m-1) > h:
                    return m
                j = m-1
            elif hours > h:
                if calculate_hours(m+1) <= h:
                    return m+1
                i = m+1