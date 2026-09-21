class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            i += 1
        j = i
        while j < len(intervals) and newInterval[1] >= intervals[j][0]:
            j += 1
        if i == j:
            return intervals[:i] + [newInterval] + intervals[i:]
        ns = min(newInterval[0], intervals[i][0])
        ne = max(newInterval[1], intervals[j-1][1])
        return intervals[:i] + [[ns, ne]] + intervals[j:]