# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。 
# 
#  每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。 
# 
#  返回载到每一个人所需的最小船数。(保证每个人都能被船载)。 
# 
#  
# 
#  示例 1： 
# 
#  输入：people = [1,2], limit = 3
# 输出：1
# 解释：1 艘船载 (1, 2)
#  
# 
#  示例 2： 
# 
#  输入：people = [3,2,2,1], limit = 3
# 输出：3
# 解释：3 艘船分别载 (1, 2), (2) 和 (3)
#  
# 
#  示例 3： 
# 
#  输入：people = [3,5,3,4], limit = 5
# 输出：4
# 解释：4 艘船分别载 (3), (3), (4), (5) 
# 
#  提示： 
# 
#  
#  1 <= people.length <= 50000 
#  1 <= people[i] <= limit <= 30000 
#  
#  Related Topics 贪心算法 双指针 
#  👍 58 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、贪心：每次选体重最小的上船
    """
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 0:
            return 0
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            ans += 1
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().numRescueBoats(people = [3,2,2,1], limit = 3) == 3
    assert Solution().numRescueBoats(people = [3,5,3,4], limit = 5) == 4
