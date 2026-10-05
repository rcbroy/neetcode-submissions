func dailyTemperatures(temperatures []int) []int {
	ans := make([]int, len(temperatures))
	for i := len(temperatures)-1; i >= 0; i-- {
		j := i+1
		for j < len(ans) {
			if temperatures[j] > temperatures[i] {
				ans[i] = j-i
				break
			} else if ans[j] == 0 {
				ans[i] = 0
				break
			} else {
				j += ans[j]
			}
		}
	}
	return ans
}
