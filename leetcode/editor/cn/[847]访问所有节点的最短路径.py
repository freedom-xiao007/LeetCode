# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。 
# 
#  给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。 
# 
#  返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：graph = [[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一种可能的路径为 [1,0,2,0,3] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一种可能的路径为 [0,1,4,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == graph.length 
#  1 <= n <= 12 
#  0 <= graph[i].length < n 
#  graph[i] 不包含 i 
#  如果 graph[a] 包含 b ，那么 graph[b] 也包含 a 
#  输入的图总是连通图 
#  
#  Related Topics 位运算 广度优先搜索 图 动态规划 状态压缩 
#  👍 151 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        que = [[i, 1 << i, 0] for i in range(n)]
        memory = defaultdict(int)
        for i in range(n): memory[1 << i, i] = 0
        all_visited = 2 ** n - 1
        while que:
            pos, visited, steps = que.pop(0)
            if visited == all_visited:
                return steps
            for nex_pos in graph[pos]:
                nex_visited = visited | (1 << nex_pos)
                if (nex_visited, nex_pos) not in memory or memory[nex_visited, nex_pos] > steps + 1:
                    que.append([nex_pos, nex_visited, steps+1])
                    memory[nex_visited, nex_pos] = steps + 1
# leetcode submit region end(Prohibit modification and deletion)
