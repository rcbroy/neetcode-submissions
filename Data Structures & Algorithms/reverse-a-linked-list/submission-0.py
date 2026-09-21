# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        next_head = head.next
        head.next = None
        while next_head:
            temp = next_head.next
            next_head.next = head
            head = next_head
            next_head = temp
        return head
            
            
        