# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            good = 0
            if not node:
                return 0
            if node.val >= curr_max:
                good += 1
            curr_max = max(curr_max, node.val)
            good += dfs(node.left, curr_max)
            good += dfs(node.right, curr_max)
            return good
        return dfs(root, root.val)