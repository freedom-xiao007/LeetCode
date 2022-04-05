# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = [0]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  
#  Related Topics 数组 
#  👍 687 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        从最低位开始加
        如果等于10，该位置为0
        后面的一位需要加一
        最后看看有没有进位，如果有进位，需要增加最后一位为1，比如9+1=10
        """
        res = []
        carry = 1
        for num in range(len(digits) - 1, -1, -1):
            value = digits[num] + carry
            if value == 10:
                res.append(0)
                carry = 1
            else:
                res.append(value)
                carry = 0
        if carry == 1:
            res.append(1)
        res.reverse()
        # print(res)
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution().plusOne([0]) == [1]
    assert Solution().plusOne([9]) == [1, 0]
