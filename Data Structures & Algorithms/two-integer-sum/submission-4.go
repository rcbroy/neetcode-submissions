func twoSum(nums []int, target int) []int {
    complement := make(map[int]int)

	for i, n := range nums {
		if j, ok := complement[target-n]; ok {
			return []int{j, i}
		}
		complement[n] = i
	}
	return nil
}
