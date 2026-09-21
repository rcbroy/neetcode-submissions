class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            top = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if top > second:
                heapq.heappush(stones, -(top-second))
        return -sum(stones)