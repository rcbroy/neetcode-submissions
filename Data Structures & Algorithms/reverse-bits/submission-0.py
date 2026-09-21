class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n))[:1:-1]
        s += (32-len(s)) * '0'
        return int(s, 2)