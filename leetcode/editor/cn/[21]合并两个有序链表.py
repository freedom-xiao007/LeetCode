# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1290 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode()
        ans = p.next
        p1, p2 = l1, l2
        while p1 is not None and p2 is not None:
            if p2 is None or (p1 is not None and p1.val < p2.val):
                p.next = ListNode(p1.val, None)
                p1 = p1.next
            else:
                p.next = ListNode(p2.val, None)
                p2 = p2.next
            p = p.next
        return ans
# leetcode submit region end(Prohibit modification and deletion)
