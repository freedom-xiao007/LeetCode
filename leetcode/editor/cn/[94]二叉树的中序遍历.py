# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 672 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        左中右顺序
        """
        ans = []
        self._in_order(root, ans)
        return ans

    def _in_order(self, root, ans):
        if root is None:
            return
        self._in_order(root.left, ans)
        ans.append(root.val)
        self._in_order(root.right, ans)
# leetcode submit region end(Prohibit modification and deletion)
