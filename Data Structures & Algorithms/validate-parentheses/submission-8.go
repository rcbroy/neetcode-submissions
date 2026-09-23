func isValid(s string) bool {
	stack := make([]rune, 0)
	pairs := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	for _, p := range s {
		switch p {
			case '[', '{', '(':
				stack = append(stack, p)
			default:
				if len(stack) < 1 || pairs[p] != stack[len(stack)-1] {
					return false
				}
				stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}