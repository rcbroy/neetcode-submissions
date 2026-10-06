func longestConsecutive(nums []int) int {
	consecutive := make(map[int]int)
	longest := 0
	for _, n := range nums {
		if _, ok := consecutive[n]; ok {
			continue
		}
		consecutive[n] = n
		high := n
		low := n
		if higher, ok := consecutive[n+1]; ok {
			high = higher
		}
		if lower, ok := consecutive[n-1]; ok {
			low = lower
		}
		consecutive[low] = high
		consecutive[high] = low
		longest = max(longest, high - low + 1)
	}
	return longest
}
