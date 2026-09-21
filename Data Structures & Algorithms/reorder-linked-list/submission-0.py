# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = slow
        slow = slow.next
        head2.next = None
        while slow:
            temp = slow.next
            slow.next = head2
            head2 = slow
            slow = temp

        while head and head2.next:
            temp = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp
            head = temp
            head2 = temp2
