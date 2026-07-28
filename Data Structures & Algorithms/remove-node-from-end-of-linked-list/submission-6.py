# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(head)
        l, r = d, head

        while n>=0:
            r = r.next
            n -=1
        
        while r:
            l = l.next
            r = r.next
        
        left.next=left.next.next
        return d.next
        
