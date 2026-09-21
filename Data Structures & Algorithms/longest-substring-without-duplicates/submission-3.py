class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx = {}
        longest = 0
        unique = 0
        count = 0
        for i, l in enumerate(s):
            if l in idx:
                longest = max(longest, i-unique)
                print(unique, i, longest, i-unique)
                unique = max(idx[l]+1, unique)
            idx[l] = i
        return max(longest, len(s) - unique)