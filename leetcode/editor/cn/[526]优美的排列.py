# 假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，
# 我们就称这个数组为一个优美的排列。条件： 
# 
#  
#  第 i 位的数字能被 i 整除 
#  i 能被第 i 位上的数字整除 
#  
# 
#  现在给定一个整数 N，请问可以构造多少个优美的排列？ 
# 
#  示例1: 
# 
#  
# 输入: 2
# 输出: 2
# 解释: 
# 
# 第 1 个优美的排列是 [1, 2]:
#   第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
#   第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
# 
# 第 2 个优美的排列是 [2, 1]:
#   第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
#   第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
#  
# 
#  说明: 
# 
#  
#  N 是一个正整数，并且不会超过15。 
#  
#  Related Topics 位运算 数组 动态规划 回溯 状态压缩 
#  👍 150 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    def countArrangement(self, n: int) -> int:
        # 所有可选的数
        start = tuple(i for i in range(1, n + 1))

        @lru_cache(None)
        def dfs(i, available):
            # 到最后一个数了
            if i == n:
                # 最后一个位置需要是优美的
                if available[0] % i == 0 or i % available[0] == 0:
                    return 1
                return 0
            ans = 0
            for num in available:
                # 当前第i位也需要是优美的
                if num % i == 0 or i % num == 0:
                    # 去掉被使用的数
                    tmp = list(available)
                    tmp.remove(num)
                    ans += dfs(i + 1, tuple(tmp))
            return ans

        return dfs(1, start)
# leetcode submit region end(Prohibit modification and deletion)
