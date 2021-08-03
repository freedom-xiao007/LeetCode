# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。 
# 
#  请你找出符合题意的 最短 子数组，并输出它的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？ 
#  
#  
#  Related Topics 栈 贪心 数组 双指针 排序 单调栈 
#  👍 591 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # ---- 从左往右，找子数组的右边界（实指）
        sub_max = float('-inf')
        sub_r = -1
        for i, x in enumerate(nums):
            if x < sub_max:
                sub_r = i
            else:
                sub_max = x

        # ---- 从右往左，找子数组的左边界（实指）
        sub_min = float('inf')
        sub_l = -1
        for i in range(n - 1, -1, -1):
            x = nums[i]
            if x > sub_min:
                sub_l = i
            else:
                sub_min = x

        if sub_l == sub_r:
            return 0
        else:
            return sub_r - sub_l + 1
# leetcode submit region end(Prohibit modification and deletion)
