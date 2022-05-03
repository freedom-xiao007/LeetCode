# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 
# 
#  
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
# 
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
#  Related Topics 哈希表 数学 动态规划 堆（优先队列） 👍 337 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [i for i in range(0, n+1)]
        dp[1] = 1

        p2, p3, p5 = 1, 1, 1
        for i in range(2, n+1):
            n2 = dp[p2] * 2
            n3 = dp[p3] * 3
            n5 = dp[p5] * 5
            dp[i] = min(n2, n3, n5)
            if n2 == dp[i]:
                p2 += 1
            if n3 == dp[i]:
                p3 += 1
            if n5 == dp[i]:
                p5 += 1
        print(dp)
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    assert Solution().nthUglyNumber(1) == 1
    assert Solution().nthUglyNumber(10) == 12
