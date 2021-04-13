//将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
//
// 
//
// 示例： 
//
// 输入：1->2->4, 1->3->4
//输出：1->1->2->3->4->4
// 
// Related Topics 链表 
// 👍 1406 👎 0
package main

//leetcode submit region begin(Prohibit modification and deletion)
//  Definition for singly-linked list.
//type ListNode struct {
//    Val int
//    Next *ListNode
//}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}

	res := &ListNode{}
	p := res

	for l1 != nil || l2 != nil {
		if l1 == nil || (l2 != nil && l2.Val < l1.Val){
			p.Next = &ListNode{l2.Val, nil}
			l2 = l2.Next
		} else {
			p.Next = &ListNode{l1.Val, nil}
			l1 = l1.Next
		}
		p = p.Next
	}

	return res.Next
}
//leetcode submit region end(Prohibit modification and deletion)
