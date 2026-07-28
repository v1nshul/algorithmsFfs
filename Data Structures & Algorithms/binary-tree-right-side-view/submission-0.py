# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        q.append(root)
        res.append(root)

        while q:
            cur = q.popleft()
            if cur.right:
                res.append(cur.right.val)
                q.append(cur.right)
        return res
