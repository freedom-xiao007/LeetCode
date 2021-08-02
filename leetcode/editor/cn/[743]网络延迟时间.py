# 有 N 个网络节点，标记为 1 到 N。 
# 
#  给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从
# 源节点传递到目标节点的时间。 
# 
#  现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# 输出：2
#  
# 
#  
# 
#  注意: 
# 
#  
#  N 的范围在 [1, 100] 之间。 
#  K 的范围在 [1, N] 之间。 
#  times 的长度在 [1, 6000] 之间。 
#  所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。 
#  
#  Related Topics 堆 深度优先搜索 广度优先搜索 图 
#  👍 160 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connect = defaultdict(lambda:defaultdict(int))
        for u,v,w in times:
            connect[u][v] = w
        q = [(0, k)]
        explored = set()
        while q:
            t, node = heapq.heappop(q)
            if node in explored:
                continue
            explored.add(node)
            if len(explored) == n:
                return t
            for other, tm in connect[node].items():
                if other not in explored:
                    heapq.heappush(q, (t+tm, other))
        return -1
# leetcode submit region end(Prohibit modification and deletion)
