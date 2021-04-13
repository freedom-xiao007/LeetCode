"""
5521. 矩阵的最大非负积 显示英文描述
通过的用户数240
尝试过的用户数425
用户总通过次数242
用户总提交次数797
题目难度Medium
给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。

在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。

返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为负数，则返回 -1 。

注意，取余是在得到最大积之后执行的。



示例 1：

输入：grid = [[-1,-2,-3],
             [-2,-3,-3],
             [-3,-3,-2]]
输出：-1
解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
示例 2：

输入：grid = [[1,-2,1],
             [1,-2,1],
             [3,-4,1]]
输出：8
解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
示例 3：

输入：grid = [[1, 3],
             [0,-4]]
输出：0
解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
示例 4：

输入：grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]
输出：2
解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)


提示：

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4
"""
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[[]]] * len(grid)
        dp[0][0].append([grid[0][0], grid[0][0]])
        for item in dp:
            print(item)
        for i in range(0, len(grid)):
            dp[i].append([[]] * len(grid[i]))
            for j in range(0, len(grid[i])):
                print(i, j, dp[i][j])
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] += [grid[i][j-1] * grid[i][j], grid[i][j-1] * grid[i][j]]
                elif j == 0:
                    dp[i][j] += [grid[i-1][j] * grid[i][j], grid[i-1][j] * grid[i][j]]
                else:
                    dp[i][j] += [min(grid[i][j-1][0] * grid[i][j], grid[i-1][j][0] * grid[i][j]),
                                 max(grid[i][j-1][1] * grid[i][j], grid[i-1][j][1] * grid[i][j])]
            print(dp[i][j])
        return max(dp[-1][-1])


if __name__ == "__main__":
    grid = [[1, 4, 4, 0],
            [-2, 0, 0, 1],
            [1, -1, 1, 1]]
    assert Solution().maxProductPath(grid) == 2
