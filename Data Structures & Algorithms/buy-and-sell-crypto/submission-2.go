func maxProfit(prices []int) int {
	i := 0
	curr_max := 0
	for j := range prices {
		if prices[j] < prices[i] {
			i = j
			continue
		}
		curr_max = max(curr_max, prices[j]-prices[i])
	}
	return curr_max
}
