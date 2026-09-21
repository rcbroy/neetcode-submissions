class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        ordered = list(counts.keys())
        ordered.sort(key=lambda x: counts[x], reverse=True)
        return ordered[:k]
        