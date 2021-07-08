# 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。 
# 
#  你可以搭配 任意 两道餐品做一顿大餐。 
# 
#  给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大
# 餐 的数量。结果需要对 109 + 7 取余。 
# 
#  注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：deliciousness = [1,3,5,7,9]
# 输出：4
# 解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
# 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
#  
# 
#  示例 2： 
# 
#  
# 输入：deliciousness = [1,1,1,3,3,3,7]
# 输出：15
# 解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= deliciousness.length <= 105 
#  0 <= deliciousness[i] <= 220 
#  
#  Related Topics 数组 哈希表 
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    mod = 10 ** 9 + 7
    maximum = 1 << 22
    def countPairs(self, deliciousness: List[int]) -> int:
        hashmap = Counter(deliciousness)
        ans = 0
        for x in hashmap:
            i = 1
            while i < self.maximum:
                t = i - x
                if t in hashmap:
                    if t == x:
                        ans += (hashmap[x] - 1) * hashmap[x]
                    else:
                        ans += hashmap[x] * hashmap[t]
                i <<= 1
        ans >>= 1
        return ans % self.mod

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    "https://leetcode-cn.com/problems/count-good-meals/solution/gong-shui-san-xie-xiang-jie-san-chong-gu-nn4f/"
    assert Solution().countPairs([1, 3, 5, 7, 9]) == 4
    assert Solution().countPairs([1, 1, 1, 3, 3, 3, 7]) == 15
