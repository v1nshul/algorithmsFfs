# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                res.append(-1)
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        res.sort()

        for i in res:
            if i == -1:
                res.remove(i)
        return res[k-1]
        