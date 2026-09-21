# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        cache = dict()
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            if node not in cache:
                left = dfs(node.left) + node.val
                right = dfs(node.right) + node.val
                cache[node] = max(left, right, node.val)
                max_path = max(max_path, left+right-node.val, cache[node])
            return cache[node]
        dfs(root)
        return max_path
            