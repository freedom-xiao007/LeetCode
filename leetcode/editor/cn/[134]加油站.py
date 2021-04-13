# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。 
# 
#  你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。 
# 
#  如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。 
# 
#  说明: 
# 
#  
#  如果题目有解，该答案即为唯一答案。 
#  输入数组均为非空数组，且长度相同。 
#  输入数组中的元素均为非负数。 
#  
# 
#  示例 1: 
# 
#  输入: 
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# 
# 输出: 3
# 
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。 
# 
#  示例 2: 
# 
#  输入: 
# gas  = [2,3,4]
# cost = [3,4,3]
# 
# 输出: -1
# 
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。 
#  Related Topics 贪心算法 
#  👍 380 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一：先选择从剩余油量最多的开始出发，剩余油量的gas【i】-cost【i】
    剪枝：油量小于0则结束
    如果题目中没有i只能开往i+1的限制，则判断整个剩余油量和返回最大剩余油量的加油站即可

    有i开往i+1的限制时，整个剩余油量小于0的话肯定是不能完成一圈的
    1.循环遍历数据，作为出发点；剩余油量不足的排除
    2.往后逐步计算返回到出发点的油量是否不小于0；过程中出现油量小于0则提前淘汰
    3.能返回出发点返回结果；都不能则返回-1

    注：一个加油也要开出去？这样的话一个的话就需要判断，不能直接认为能完成了

    二：如果总的剩余油量大于等于0则表明，存在一条路径能完成，证明不太会，但至少是找不到反例
    1.判断总剩余流量，小于0则返回-1
    2.从0开始遍历，计算从当前位置出发的剩余流量，如果当前剩余小于0，设置下一个加油站为出发点
    3.返回出发点
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sizeGas, sizeCost = len(gas), len(cost)

        remains = 0
        for i in range(0, sizeGas):
            remains += gas[i] - cost[i]
        if remains < 0:
            return -1

        cur = 0
        ans = 0
        for i in range(0, sizeGas):
            cur += gas[i] - cost[i]
            if cur < 0:
                ans = i + 1
                cur = 0
        return ans

    def _judgeCycle(self, start, next, remain, gas, cost, size):
        if next >= size:
            next = 0
        if next == start:
            return True

        remain = remain + (gas[next] - cost[next])
        if remain < 0:
            return False
        return self._judgeCycle(start, next+1, remain, gas, cost, size)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3,4,5,1,2]
    print(Solution().canCompleteCircuit(gas, cost))

    gas = [3, 1, 1]
    cost = [1, 2, 2]
    print(Solution().canCompleteCircuit(gas, cost))

    gas = [5, 8, 2, 8]
    cost = [6, 5, 6, 6]
    print(Solution().canCompleteCircuit(gas, cost))
