func dailyTemperatures(temperatures []int) []int {
	idxs := make([]int, 0, len(temperatures))
	ans := make([]int, len(temperatures))
	for i, t := range temperatures {
		for len(idxs) > 0 && temperatures[idxs[len(idxs)-1]] < t {
			idx := idxs[len(idxs)-1]
			ans[idx] = i-idx
			idxs = idxs[:len(idxs)-1]
		}
		idxs = append(idxs, i)
	}
	return ans
}
