func dailyTemperatures(temperatures []int) []int {
	stack := make([]int, 0, len(temperatures))
	idxs := make([]int, 0, len(temperatures))
	ans := make([]int, len(temperatures))
	for i, t := range temperatures {
		for len(stack) > 0 && stack[len(stack)-1] < t {
			idx := idxs[len(idxs)-1]
			ans[idx] = i-idx
			stack = stack[:len(stack)-1]
			idxs = idxs[:len(idxs)-1]
		}
		stack = append(stack, t)
		idxs = append(idxs, i)
	}
	return ans
}
