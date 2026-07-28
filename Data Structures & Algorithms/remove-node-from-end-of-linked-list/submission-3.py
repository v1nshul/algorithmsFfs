# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c= head
        p = None

        while c:
            t = c.next
            c.next =p
            p = c
            c = t
        
        i = 0
        tmp = None
        while p and i <= n-1:
            i += 1
            tmp = p
            p = p.next
            if i == n-1:
                t = p.next
                p = tmp
                p.next = t
                break
        
        pr = None
        c = p
        while c:
            t = c.next
            c.next = pr
            pr = c
            c = t
        return pr


