/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    if list1 != nil && list2 != nil {
		if list1.Val > list2.Val {
			list2.Next = mergeTwoLists(list2.Next, list1)
			return list2
		}
		list1.Next = mergeTwoLists(list1.Next, list2)
		return list1
	} else if list1 == nil {
		return list2
	} else {
		return list1
	}
}
