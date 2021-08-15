# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以
# 穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。 
# 
#  给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 
# 109 + 7 取余 后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 50 
#  0 <= maxMove <= 50 
#  0 <= startRow < m 
#  0 <= startColumn < n 
#  
#  Related Topics 动态规划 
#  👍 141 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(N + 1)]

        for r in range(m + 2):
            dp[0][r][0] = 1
            dp[0][r][n + 1] = 1

        for c in range(n + 2):
            dp[0][0][c] = 1
            dp[0][m + 1][c] = 1

        for k in range(1, N + 1):
            for r in range(1, m + 1):
                for c in range(1, n + 1):
                    dp[k][r][c] = dp[k - 1][r - 1][c] + dp[k - 1][r + 1][c] + dp[k - 1][r][c - 1] + dp[k - 1][r][c + 1]
        res = 0
        for k in range(1, N + 1):
            res += dp[k][i + 1][j + 1]
        return res % (10 ** 9 + 7)
# leetcode submit region end(Prohibit modification and deletion)
