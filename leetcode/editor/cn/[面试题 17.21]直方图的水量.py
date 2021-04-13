# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marco
# s 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 77 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        self._scanAndCal(0, len(height), height)
        self._scanAndCal(0, len(height), height)

    def _scanAndCal(self, param, param1, height):
        left, right = 0, 0
        for i in range(0, len(height)):
            if height[right]

# leetcode submit region end(Prohibit modification and deletion)
