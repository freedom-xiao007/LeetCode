"""
36. 有效的数独
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
示例 2:

输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
说明:

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。
通过次数85,492提交次数141,765
在真实的面试中遇到过这道题？
贡献者
LeetCode


解题思路：
1.暴力解：3次循环判断即可，用hash存值，有重复的就返回False
2.官方题解中的一次遍历，其中的3x3的box_index是精髓，这个得记住，也是用hash存值，重复判断
    - box_index = (row / 3) * 3 + columns / 3：需要好好体会
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(0, 9)]
        cols = [{} for i in range(0, 9)]
        boxs = [{} for i in range(0, 9)]

        for i in range(0, 9):
            for j in range(0, 9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    # Python3的整除
                    boxIndex = int((i // 3) * 3 + j // 3)

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxs[boxIndex][num] = boxs[boxIndex].get(num, 0) + 1

                    print(i, j, boxIndex, num, rows[i][num], cols[j][num], boxs[boxIndex][num])
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxs[boxIndex][num] > 1:
                        return False
        return True


if __name__ == "__main__":
    s = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(s.isValidSudoku(board))
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(s.isValidSudoku(board))

    board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
             ["2", ".", ".", ".", ".", ".", ".", ".", "."],
             ["3", ".", ".", ".", ".", ".", ".", ".", "."],
             ["4", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", ".", "."],
             ["6", ".", ".", ".", ".", ".", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             ["8", ".", ".", ".", ".", ".", ".", ".", "."],
             ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
    print(s.isValidSudoku(board))
