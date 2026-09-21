import (
	"cmp"
	"slices"
)

func topKFrequent(nums []int, k int) []int {
	counts := make(map[int]int)
	for _, n := range nums {
		counts[n]++
	}
	type Pair struct {
		key int
		value int
	}
	pairs := make([]Pair, 0, len(counts))
	for k, v := range counts {
		pairs = append(pairs, Pair{k, v})
	}
	slices.SortFunc(pairs, func(a, b Pair) int { 
		return cmp.Compare(b.value, a.value)
	})
	ans := make([]int, 0, k)
	for i := range k {
		ans = append(ans, pairs[i].key)
	}
	return ans
}
