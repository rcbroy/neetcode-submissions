func evalRPN(tokens []string) int {
	stack := []int{}

	for _, t := range tokens {
		switch t {
			case "+":
				left, right := stack[len(stack)-2], stack[len(stack)-1]
				stack = append(stack[:len(stack)-2], left+right)
			case "-":
				left, right := stack[len(stack)-2], stack[len(stack)-1]
				stack = append(stack[:len(stack)-2], left-right)
			case "*":
				left, right := stack[len(stack)-2], stack[len(stack)-1]
				stack = append(stack[:len(stack)-2], left*right)
			case "/":
				left, right := stack[len(stack)-2], stack[len(stack)-1]
				stack = append(stack[:len(stack)-2], left/right)
			default:
				num, err := strconv.Atoi(t)
				if err != nil {
					return 0
				}
				stack = append(stack, num)
		}
	}
	return stack[0]
}
