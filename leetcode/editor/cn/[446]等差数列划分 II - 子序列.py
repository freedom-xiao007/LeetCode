# 给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。 
# 
#  如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。 
# 
#  
#  例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。 
#  再例如，[1, 1, 2, 5, 7] 不是等差序列。 
#  
# 
#  数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。 
# 
#  
#  例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。 
#  
# 
#  题目数据保证答案是一个 32-bit 整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,4,6,8,10]
# 输出：7
# 解释：所有的等差子序列为：
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [7,7,7,7,7]
# 输出：16
# 解释：数组中的任意子序列都是等差子序列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  -231 <= nums[i] <= 231 - 1 
#  
#  Related Topics 数组 动态规划 
#  👍 137 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = [defaultdict(int) for _ in range(n)]
        for r in range(1, n):
            for l in range(r):
                diff = nums[r] - nums[l]
                x = dp[l].get(diff, 0)
                res += x
                dp[r][diff] += (x+1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
