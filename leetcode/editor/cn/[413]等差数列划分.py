# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。 
# 
#  
#  例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。 
#  
# 
#  
#  
#  给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。 
# 
#  子数组 是数组中的一个连续序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：3
# 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
#  
# 
#  示例 2： 
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
#  1 <= nums.length <= 5000 
#  -1000 <= nums[i] <= 1000 
#  
#  
#  
#  Related Topics 数组 动态规划 
#  👍 267 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return 0

        ans = 0
        left = 0
        right = left + 2
        while left < size and right < size:
            count, maxr = self.find(nums, left)
            ans += count
            left = maxr
            right = left + 2
        return int(ans)

    def find(self, nums, left):
        dif = nums[left + 1] - nums[left]
        maxr = left+1
        for i in range(left+2, len(nums)):
            if dif == nums[i] - nums[i-1]:
                maxr = i
            else:
                break
        if maxr - left >= 2:
            size = maxr - left + 1
            return (size-2) * (size - 1) / 2, maxr
        return 0, left + 1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    assert Solution().numberOfArithmeticSlices([1,2,3]) == 1
    assert Solution().numberOfArithmeticSlices([1,2]) == 0
    assert Solution().numberOfArithmeticSlices([1,2,8,10]) == 0
    assert Solution().numberOfArithmeticSlices([1,2,3,8,9,10]) == 2
    assert Solution().numberOfArithmeticSlices([1,2,3,5,7]) == 2
