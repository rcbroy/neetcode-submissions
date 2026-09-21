func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1

	for left < right {
		sum := numbers[left]+numbers[right]
		if target > sum {
			left++
		} else if target < sum {
			right--
		} else {
			return []int{left+1, right+1}
		}
	}
	return nil
}
