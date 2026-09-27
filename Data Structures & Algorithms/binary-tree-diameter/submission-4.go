/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diameterOfBinaryTree(root *TreeNode) int {
    _, diameter := helper(root)
	return diameter
}

func helper(root *TreeNode) (height int, maxDiameter int) {
	if root == nil {
		return 0, 0
	}
	left, maxDLeft := helper(root.Left)
	right, maxDRight := helper(root.Right)
	height = max(left, right) + 1
	maxDiameter = max(left+right, maxDLeft, maxDRight)
	return height, maxDiameter
}