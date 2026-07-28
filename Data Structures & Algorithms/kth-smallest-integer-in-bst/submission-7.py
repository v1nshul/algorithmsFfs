# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def dfs(root,k):
            nonlocal res
            if not root:
                return
            while k > 0:
                res = root.val
                dfs(root.left,k-1)
            return res
        dfs(root.left,k)
