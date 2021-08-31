# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。 
# 
#  子数组 定义为原数组中的一个连续子序列。 
# 
#  请你返回 arr 中 所有奇数长度子数组的和 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,4,2,5,3]
# 输出：58
# 解释：所有奇数长度子数组和它们的和为：
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# 我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58 
# 
#  示例 2： 
# 
#  输入：arr = [1,2]
# 输出：3
# 解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。 
# 
#  示例 3： 
# 
#  输入：arr = [10,11,12]
# 输出：66
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 100 
#  1 <= arr[i] <= 1000 
#  
#  Related Topics 数组 前缀和 
#  👍 79 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # 长度为n的数组，第一位出现在多少个奇数长度的子数组？
        # 1, 3, 5, ..., length-1/length
        # (length + 1)//2
        n = len(arr)
        l, r, ans, times = 0, n - 1, 0, (n+1) // 2
        while l <= r:
            # 对称性，前后对称位置出现的次数一样
            if l < r:
                ans += times * (arr[l] + arr[r])
            else:
                ans += times * arr[l]
            l += 1
            r -= 1
            # 下一个数比前一个数多了后一个数构成的不带前一个数的奇数子数组的个数
            times += (n - l + 1) // 2
            # 下一个数比前一个数少了前一个数构成的不带后一个数的奇数子数组的个数
            times -= (l + 1) // 2
        return ans
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    assert Solution().sumOddLengthSubarrays([1,4,2,5,3]) == 58
    assert Solution().sumOddLengthSubarrays([1,2]) == 3
    assert Solution().sumOddLengthSubarrays([10,11,12]) == 66
