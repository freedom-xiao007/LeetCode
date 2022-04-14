# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表 
#  👍 449 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        小顶堆：
        最上方为当前最小值
        如果当前值大于堆顶，弹出堆顶，插入当前值，当前值插入后，比较向前进
        如果元素个数小于K，则直接插入
        """
        statistics = {}
        for num in nums:
            statistics[num] = statistics.get(num, 0) + 1
        # print(statistics)

        minHeap = MinHeap(k)
        for key in statistics.keys():
            minHeap.push({"key": key, "value": statistics[key]})
        # print(minHeap)

        ans = []
        while minHeap.next():
            ans.append(minHeap.pop())
        # print("ans:", ans)
        return ans


class MinHeap:
    def __init__(self, size: int):
        self.size = size
        self.currentSize = 0
        self.arr = [i for i in range(0, size)]

    def next(self):
        return self.currentSize > 0

    def pop(self) -> int:
        if self.currentSize > 0:
            self.currentSize -= 1
            # print("pop:", self.arr[self.currentSize]["key"])
            return self.arr[self.currentSize]["key"]
        return None

    def push(self, value: map):
        if self.currentSize < self.size:
            self.arr[self.currentSize] = value
            self.currentSize += 1
        elif value["value"] <= self.arr[self.currentSize - 1]["value"]:
            return

        self.arr[self.currentSize - 1] = value
        t, b = self.currentSize - 1, self.currentSize - 2
        while t > 0:
            if self.arr[t]["value"] > self.arr[b]["value"]:
                self.arr[t], self.arr[b] = self.arr[b], self.arr[t]
                t, b = t - 1, b - 1
            else:
                break


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    print(Solution().topKFrequent(nums=[1], k=1))
    print(Solution().topKFrequent(nums=[5,3,1,1,1,3,73,1], k=2))
