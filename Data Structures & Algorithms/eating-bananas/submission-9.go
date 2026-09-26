import "slices"

func minEatingSpeed(piles []int, h int) int {
	slices.Sort(piles)
	left, right := 1, piles[len(piles)-1]
	for left < right {
		mid := (left + right) / 2
		if !canFinish(piles, h, mid) {
			left = mid+1
		} else {
			right = mid
		}
	}
	return right
}

func canFinish(piles []int, h int, rate int) bool {
	total := 0
	for _, p := range piles {
		total += (p / rate)
		if p % rate != 0 {
			total += 1
		}
		if total > h {
			return false
		}
	}
	return true
}
