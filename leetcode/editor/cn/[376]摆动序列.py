# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。 
# 
#  例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,
# 4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。 
# 
#  给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。 
# 
#  示例 1: 
# 
#  输入: [1,7,4,9,2,5]
# 输出: 6 
# 解释: 整个序列均为摆动序列。
#  
# 
#  示例 2: 
# 
#  输入: [1,17,5,10,13,15,10,5,16,8]
# 输出: 7
# 解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。 
# 
#  示例 3: 
# 
#  输入: [1,2,3,4,5,6,7,8,9]
# 输出: 2 
# 
#  进阶: 
# 你能否用 O(n) 时间复杂度完成此题? 
#  Related Topics 贪心算法 动态规划 
#  👍 231 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、贪心：根据摆动序列的特点，其是一个中心开花的两边差值相互交替的，而且差值数必为奇数，则原始数必为偶数
    样例：1，-1,1，0,1,-1,1 样例：1，-1,1,2,2，-1,1，-1
    1.如果出现[i] == [j]（差值为0） 那摆动序列必不可能同时包含着两个数，摆动序列必在【:j】和【j:】这两个子数组中
    2.如果出现不符合规则：1,1（正正），-1，-1（负负），则摆动序列必不可能不含这两个数，摆动序列必在其左右部分
    这种思路失败了。。。。

    二、求波峰波谷：这位老哥厉害，问题转化能力NB
    边界条件：[], [0,0], [0]
    """
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        pre, cur, ans = 0, 0, 1
        for i in range(1, size):
            cur = nums[i] - nums[i-1]
            if (cur < 0 <= pre) or (cur > 0 >= pre):
                ans += 1
                pre = cur
        # print(ans)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().wiggleMaxLength([1,7,4,9,2,5]) == 6
    assert Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7
    assert Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2
