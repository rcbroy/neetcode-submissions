class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([b for b in bin(n) if b == '1'])