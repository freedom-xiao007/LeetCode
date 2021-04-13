# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 
# 的朋友。所谓的朋友圈，是指所有朋友的集合。 
# 
#  给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你
# 必须输出所有学生中的已知的朋友圈总数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出：2 
# 解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回 2 。
#  
# 
#  示例 2： 
# 
#  输入：
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出：1
# 解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 200 
#  M[i][i] == 1 
#  M[i][j] == M[j][i] 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 314 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、此题和岛屿类似，套用岛屿的解题思路，联通1及其周围的1即可
    消除的思路是如果当前[i][j]为1，则消除i的朋友（i的朋友为已i为行，已i为列的数据，也就是已i为十字中心进行消除），j的朋友
    时间复杂度应该是O(N^3)，消除当前位置就需要消除其所在的行和列，为2N，加上外层N**2

    二、并查集:其核心思想就是将有关系的两个人，让第二个人的父亲认第一个人的父亲做父亲，虽然开始降了辈分，但后面扁平化后大家也会成同辈
    1.各自自立山头，自成老祖
    2.两个人之间有关系，让第二个人的老祖认第一个人的老祖做老祖，同时后面扁平化处理
    3.遍历查看老祖数量（自己老祖是自己的才是真老祖），返回数量
    时间复杂度应该是O(N^3)
    """

    def findCircleNum(self, M: List[List[int]]) -> int:
        """方法二：并查集"""
        parents = [i for i in range(0, len(M))]
        for i in range(0, len(M)):
            for j in range(0, len(M[i])):
                if i != j and M[i][j] == 1:
                    self._union(parents, i, j)
        ans = 0
        for i in range(0, len(parents)):
            if parents[i] == i:
                ans += 1
        return ans

    def _union(self, parents, i, j):
        pi = self._findParent(parents, i)
        pj = self._findParent(parents, j)
        parents[pj] = pi

    def _findParent(self, parents, index):
        root = index
        while parents[root] != root:
            root = parents[root]
        while parents[index] != index:
            temp = parents[index]
            parents[index] = root
            index = temp
        return root

    def _methodOne(self, M: List[List[int]]):
        """方法一"""
        ans = 0
        w, h = len(M[0]), len(M)
        for i in range(0, h):
            for j in range(0, h):
                if M[i][j] == 1:
                    ans += 1
                    self._dfs(M, i, h, w)
                    self._dfs(M, j, h, w)
        return ans

    def _dfs(self, M, index, h, w):
        """消除以第index个人的所有朋友，置零，及十字中心扩展消除"""
        if index < 0 or index >= h:
            return
        for col in range(0, w):
            if M[index][col] == 1:
                M[index][col] = 0
                self._dfs(M, col, h, w)
        for row in range(0, h):
            if M[row][index] == 1:
                M[row][index] = 0
                self._dfs(M, row, h, w)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    print(Solution().findCircleNum(M))
    M = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 1, 1]]
    print(Solution().findCircleNum(M))
