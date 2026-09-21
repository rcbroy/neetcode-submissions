# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length == n:
            return head.next
        node = head
        length = length - 1 - n
        while length > 0:
            node = node.next
            length -= 1
        node.next = node.next.next
        return head