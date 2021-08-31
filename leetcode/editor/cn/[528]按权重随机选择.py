# 给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标 i，选取下标 
# i 的概率与 w[i] 成正比。 
# 
#  
#  
# 
#  例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 +
#  3) = 0.75（即，75%）。 
# 
#  也就是说，选取下标 i 的概率为 w[i] / sum(w) 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# ["Solution","pickIndex"]
# [[[1]],[]]
# 输出：
# [null,0]
# 解释：
# Solution solution = new Solution([1]);
# solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。 
# 
#  示例 2： 
# 
#  输入：
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# 输出：
# [null,1,1,1,1,0]
# 解释：
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
# solution.pickIndex(); // 返回 1
# solution.pickIndex(); // 返回 1
# solution.pickIndex(); // 返回 1
# solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。
# 
# 由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# 诸若此类。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= w.length <= 10000 
#  1 <= w[i] <= 10^5 
#  pickIndex 将被调用不超过 10000 次 
#  
#  Related Topics 数学 二分查找 前缀和 随机化 
#  👍 116 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self, A):
        # 更新数组，用于存储累计和，即截至当前数字累计的权重
        # 例如[1, 4, 7] -> [1, 5, 12]
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        self.A = A

    def pickIndex(self) -> int:
        # 随机抽取 1至self.A[-1]之间的一个整数
        target = random.randint(1, self.A[-1])
        # bisect：基于二分查找实现各种功能的库
        # bisect.bisect(A, target)， 在已经排好序的数组A中，寻找需插入target的索引位置
        # _left：有重复值时，插在相等的元素的左侧，例如[1, 5, 12]中，target取2~5时，都返回下标1
        return bisect.bisect_left(self.A, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# leetcode submit region end(Prohibit modification and deletion)
