class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ns = set()
        for n in nums:
            if n in ns:
                return True
            ns.add(n)
        return False