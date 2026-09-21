class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = defaultdict(int)
        dt = defaultdict(int)
        for letter in s:
            ds[letter] += 1
        for letter in t:
            dt[letter] += 1

        return ds == dt