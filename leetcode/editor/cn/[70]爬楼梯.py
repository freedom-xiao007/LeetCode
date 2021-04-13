# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1223 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一.动态规划：
    1.重复子问题：跳动当前位置的数量为前两个位置之和
    2.递推状态：dp【i】
    3.递推公式：dp[i] = dp[i-1] + dp[i-2]
    遍历一次，时间复杂度O(N)
    """
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n < 3:
            return dp[n-1]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
