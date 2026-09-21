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
        # def dfs(node, level):
        #     if node:
        #         if len(ans) < level+1:
        #             ans.append([])
        #         ans[level].append(node.val)
        #         dfs(node.left, level+1)
        #         dfs(node.right, level+1)
        # dfs(root, 0)
        # return ans
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            while len(ans) < level+1:
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return ans