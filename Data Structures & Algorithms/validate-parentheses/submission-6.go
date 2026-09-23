func isValid(s string) bool {
    stack := Stack{idx: -1}

	for _, p := range s {
		switch p {
			case '{':
				stack.push("{")
			case '[':
				stack.push("[")
			case '(':
				stack.push("(")
			case ')':
				if stack.pop() != "(" {
					return false
				}
			case '}':
				if stack.pop() != "{" {
					return false
				}
			case ']':
				if stack.pop() != "[" {
					return false
				}
		}
	}
	return stack.isEmpty()
}

type Stack struct {
	items	[]string
	idx 	int
}

func (s *Stack) peek() string {
	if s.idx == -1 {
		return ""
	} else {
		return s.items[s.idx]
	}
}

func (s *Stack) push(item string) {
	s.idx++
	s.items = append(s.items, item)
}

func (s *Stack) pop() string {
	if s.idx == -1 {
		return ""
	} else {
		item := s.items[s.idx]
		s.idx--
		s.items = s.items[:len(s.items)-1]
		return item
	}
}

func (s *Stack) isEmpty() bool {
	return s.idx == -1
}
