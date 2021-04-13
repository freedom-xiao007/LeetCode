# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 942 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、动态规律:参考官方题解
    1.重复子结构：（）的求职很好理解，（（）（））的求值需要自己按照公式进行推导后就理解了
    2.递推状态：dp【i】
    3.递推公式：（）-->dp[i]=2,))-->dp[i] = dp[i-1]+2 + dp[i-dp[i-1]-1]
    注：注意边界条件的判断和加上有效括号前一个连续有效括号的长度
    遍历一次，时间复杂度为O(N)

    二、用栈和括号的有效性结合：方法很巧妙,时间复杂度为O(N)
    """

    def longestValidParentheses(self, s: str) -> int:
        size = len(s)
        dp = [0] * size
        ans = 0
        for i in range(1, size):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2
                    if i - 2 >= 0:
                        dp[i] += dp[i - 2]
                    ans = max(ans, dp[i])
                elif s[i - 1] == ")" and dp[i - 1] > 0 and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
                    ans = max(ans, dp[i])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
