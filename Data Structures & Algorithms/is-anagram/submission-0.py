class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)
        for l in s:
            letters[l] += 1
        for k in  t:
            letters[k] -= 1
        return not any(letters.values())