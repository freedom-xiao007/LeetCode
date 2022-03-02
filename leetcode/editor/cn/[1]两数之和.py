# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 8956 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    """
    解题思路：
    一、排序加双指针，O(NlogN)
    二、一次遍历哈希统计比较，O(N)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        cal_cache = {target - nums[0]: 0}
        for i in range(1, len(nums)):
            num = nums[i]
            if num in cal_cache:
                return [cal_cache[num], i]
            cal_cache[target - num] = i
        return []
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert [0, 1] == Solution().twoSum(nums=[2, 7, 11, 15], target=9)
