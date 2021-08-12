# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 13
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 2 * 109 
#  
#  Related Topics 递归 数学 动态规划 
#  👍 243 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        divider, count = 1, 0
        while divider <= n:
            count += (n // (divider * 10)) * divider + min(max(n % (divider * 10) - divider + 1, 0), divider)
            divider *= 10
        return count
# leetcode submit region end(Prohibit modification and deletion)
