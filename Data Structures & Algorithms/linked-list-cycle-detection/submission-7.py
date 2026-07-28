# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        c = head
        s = set()

        while c:
            t = c.next
            if t in s:
                return True
            c = t
        return -1
    