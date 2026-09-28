/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isBalanced(root *TreeNode) bool {
    balanced := true
	var height func(root *TreeNode) int
	height = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left, right := height(root.Left), height(root.Right)
		if right-left > 1 || left-right > 1 {
			balanced = false
		}
		return max(left, right) + 1
	}
	height(root)
	return balanced
}
