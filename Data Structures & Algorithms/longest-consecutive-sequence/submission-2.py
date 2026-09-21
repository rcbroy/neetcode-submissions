class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c = set()
        for n in nums:
            c.add(n)
        max_length = 1
        def length(m, c):
            count = 1
            n = m
            c.discard(m)
            while m+1 in c:
                m += 1
                count += 1
                c.discard(m)
            while n-1 in c:
                n -= 1
                count += 1
                c.discard(n)
            return count

        while c and len(c) > max_length:
            m = c.pop()
            curr = length(m, c)
            if curr > max_length:
                max_length = curr
        return max_length
            
        