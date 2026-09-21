# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def order(node, level):
            if node:
                if len(ans) < level+1:
                    ans.append([])
                ans[level].append(node.val)
                order(node.left, level+1)
                order(node.right, level+1)
        order(root, 0)
        return ans
