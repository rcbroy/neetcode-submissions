/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    if head != nil && head.Next != nil {
		temp := head.Next
		newHead := reverseList(head.Next)
		temp.Next = head
		head.Next = nil
		return newHead
	}
	return head
}
