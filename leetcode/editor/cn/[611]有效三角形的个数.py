# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。 
# 
#  示例 1: 
# 
#  
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是: 
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
#  
# 
#  注意: 
# 
#  
#  数组长度不超过1000。 
#  数组里整数的范围为 [0, 1000]。 
#  
#  Related Topics 贪心 数组 双指针 二分查找 排序 
#  👍 200 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()

        ans = 0
        for i in range(0, length):
            x = nums[i]
            r = i + 1
            for j in range(i + 1, length):
                y = nums[j]
                while r + 1 < length and x + y > nums[r + 1]:
                    r += 1
                cur = max(0, r - j)
                ans += cur
        return ans
# leetcode submit region end(Prohibit modification and deletion)
