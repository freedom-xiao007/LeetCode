# 存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数： 
# 
#  
#  如果 nums[i] 是正数，向前 移动 nums[i] 步 
#  如果 nums[i] 是负数，向后 移动 nums[i] 步 
#  
# 
#  因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。 
# 
#  数组中的 循环 由长度为 k 的下标序列 seq ： 
# 
#  
#  遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ... 
#  所有 nums[seq[j]] 应当不是 全正 就是 全负 
#  k > 1 
#  
# 
#  如果 nums 中存在循环，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,-1,1,2,2]
# 输出：true
# 解释：存在循环，按下标 0 -> 2 -> 3 -> 0 。循环长度为 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [-1,2]
# 输出：false
# 解释：按下标 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
#  
# 
#  示例 3: 
# 
#  
# 输入：nums = [-2,1,-1,-2,-2]
# 输出：false
# 解释：按下标 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为 nums[1] 是正数，而 nums[2] 是负数。
# 所有 nums[seq[j]] 应当不是全正就是全负。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -1000 <= nums[i] <= 1000 
#  nums[i] != 0 
#  
# 
#  
# 
#  进阶：你能设计一个时间复杂度为 O(n) 且额外空间复杂度为 O(1) 的算法吗？ 
#  Related Topics 数组 哈希表 双指针 
#  👍 108 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        # x的下一个位置
        nxt = lambda x: (x + nums[x]) % n

        for i in range(n):
            if nums[i] == 0: continue
            slow = i
            fast = nxt(i)
            # 快慢指针
            """符号相同保证是同一个方向移动"""
            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nxt(fast)] > 0:
                """快指针每次走两步，如果快慢指针相等，说明有环"""
                if slow == fast:
                    """如果是自身环，那么退出循环"""
                    if slow == nxt(slow):
                        break
                    else:
                        return True
                """更新状态，快指针每次走两步"""
                slow = nxt(slow)
                fast = nxt(nxt(fast))
            # 访问过的置0
            """如果上面那轮没有return，说明上面遍历过的元素都不可能成环，为避免再次遍历陷入无效查找，故将查找过的元素置零，再次遍历时直接跳过"""
            while nums[i] > 0:
                """先找到下一个元素的index"""
                tmp = nxt(i)
                """将当前的元素置零"""
                nums[i] = 0
                """向下走一步"""
                i = tmp
        return False
# leetcode submit region end(Prohibit modification and deletion)
