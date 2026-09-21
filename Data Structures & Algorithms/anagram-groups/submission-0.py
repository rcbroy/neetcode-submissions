class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            word = ''.join(sorted(s))
            anagrams[word].append(s)
        return anagrams.values()