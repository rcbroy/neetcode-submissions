func hammingWeight(n int) int {
	ans := 0
	for n != 0 {
		ans += (n & 1)
		n >>= 1
	}
	return ans
}
