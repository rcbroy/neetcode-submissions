func search(nums []int, target int) int {
	left, right := 0, len(nums)-1

	for left <= right {
		mid := (left + right) / 2
		if nums[mid] < target {
			if target <= nums[right] {
				left = mid + 1
			} else if nums[mid] <= nums[right] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else if target < nums[mid] {
			if nums[left] <= target {
				right = mid - 1
			} else if nums[left] <= nums[mid] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		} else {
			return mid
		}
	}
	return -1
}