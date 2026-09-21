# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 and n2 or n1 and not n2:
                return False
            else:
                return n1.val == n2.val and sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)

        if sameTree(root, subRoot):
            return True
        elif root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False