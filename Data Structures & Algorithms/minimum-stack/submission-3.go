type MinStack struct {
	items	[]int
	mins	[]int
	currMin	int
}

func Constructor() MinStack {
	return MinStack{
		items: []int{}, 
		mins: []int{},
		currMin: 0,
	}
}

func (this *MinStack) Push(val int) {
	this.items = append(this.items, val)
	if len(this.mins) > 0 && this.currMin <= val {
		this.mins = append(this.mins, this.currMin)
	} else {
		this.mins = append(this.mins, val)
		this.currMin = val
	}
}

func (this *MinStack) Pop() {
	this.items = this.items[:len(this.items)-1]
	if len(this.mins) > 1 {
		this.currMin = this.mins[len(this.mins)-2]
	} else {
		this.currMin = 0
	}
	this.mins = this.mins[:len(this.mins)-1]
}

func (this *MinStack) Top() int {
	if len(this.mins) > 0 {
		return this.items[len(this.items)-1]
	}
	return 0
}

func (this *MinStack) GetMin() int {
	return this.currMin
}
