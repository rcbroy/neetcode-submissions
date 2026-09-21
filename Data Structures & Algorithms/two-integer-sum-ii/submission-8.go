func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1

	for left < right {
		if target > (numbers[left]+numbers[right]) {
			left++
		} else if target < (numbers[left]+numbers[right]) {
			right--
		} else {
			return []int{left+1, right+1}
		}
	}
	return nil
}
