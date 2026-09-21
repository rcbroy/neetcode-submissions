// import (
// 	"cmp"
// 	"slices"
// )

func topKFrequent(nums []int, k int) []int {
	counts := make(map[int]int)
	for _, n := range nums {
		counts[n]++
	}
	// type Pair struct {
	// 	key int
	// 	value int
	// }
	// pairs := make([]Pair, 0, len(counts))
	// for key, val := range counts {
	// 	pairs = append(pairs, Pair{key, val})
	// }
	// slices.SortFunc(pairs, func(a, b Pair) int { 
	// 	return cmp.Compare(b.value, a.value)
	// })
	// ans := make([]int, 0, k)
	// for i := range k {
	// 	ans = append(ans, pairs[i].key)
	// }
	// return ans
	buckets := make([][]int, len(nums)+1)

	for k, v := range counts {
		buckets[v] = append(buckets[v], k)
	}

	ans := make([]int, 0, k)
	for i := len(nums); i > 0; i-- {
		for _, n := range buckets[i] {
			ans = append(ans, n)
			if len(ans) == k {
				return ans
			}
		}
	}
	return nil
}
