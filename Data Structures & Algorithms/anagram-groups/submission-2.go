import "slices"

func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)
	for _, word := range strs {
		sorted := sortWord(word)
		groups[sorted] = append(groups[sorted], word)
	}
	ans := [][]string{}
	for _, words := range groups {
		ans = append(ans, words)
	}
	return ans
}

func sortWord(word string) string {
	runes := []rune(word)
	slices.Sort(runes)
	return string(runes)
}