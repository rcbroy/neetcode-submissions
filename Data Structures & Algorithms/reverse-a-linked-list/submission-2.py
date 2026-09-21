# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head_next = None
        while head.next:
            temp = head.next
            head.next = head_next
            head_next = head
            head = temp
        head.next = head_next
        return head