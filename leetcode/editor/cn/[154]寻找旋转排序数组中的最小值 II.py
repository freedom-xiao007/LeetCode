# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  请找出其中最小的元素。 
# 
#  注意数组中可能存在重复的元素。 
# 
#  示例 1： 
# 
#  输入: [1,3,5]
# 输出: 1 
# 
#  示例 2： 
# 
#  输入: [2,2,2,0,1]
# 输出: 0 
# 
#  说明： 
# 
#  
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
#  
#  Related Topics 数组 二分查找 
#  👍 183 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        size = len(nums)
        if size == 1:
            return nums[0]

        ans = nums[0]
        left, right = 0, size - 1
        while left < right:
            mid = (left + right) // 2
            ans = min(ans, nums[left])
            ans = min(ans, nums[right])
            ans = min(ans, nums[mid])

            if nums[left] == nums[mid]:
                left += 1
            elif nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
