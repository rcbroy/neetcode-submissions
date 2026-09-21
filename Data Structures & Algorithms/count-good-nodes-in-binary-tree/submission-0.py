# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 1
        def dfs(node, curr_max):
            nonlocal good
            if node.left: 
                if node.left.val >= curr_max:
                    good += 1
                dfs(node.left, max(curr_max, node.left.val))
            if node.right:
                if node.right.val >= curr_max:
                    good += 1
                dfs(node.right, max(curr_max, node.right.val))
        dfs(root, root.val)
        return good