# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node:
                leftd, lefth = helper(node.left)
                rightd, righth = helper(node.right)
                return max(lefth+righth, leftd, rightd), max(lefth, righth) +1
            return 0, 0
        return helper(root)[0]