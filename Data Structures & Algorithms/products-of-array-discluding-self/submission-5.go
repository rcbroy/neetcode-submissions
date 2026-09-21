func productExceptSelf(nums []int) []int {
	products := make([]int, len(nums))
	cumProd := 1
	for i, n := range nums {
		products[i] = cumProd
		cumProd *= n
	}
	cumProd = 1
	for i := len(nums)-1; i >= 0; i-- {
		products[i] *= cumProd
		cumProd *= nums[i]
	}
	return products
}
