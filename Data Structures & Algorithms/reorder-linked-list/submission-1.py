# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = None
        c = head

        while c:
            t = c.next
            c.next = p
            p =c 
            c = t
        
        d = ListNode()
        c = head

        while p is not None and c is not None:
            d = c
            d.next = p
            c = c.next
            p = p.next
            d = d.next
        return d
