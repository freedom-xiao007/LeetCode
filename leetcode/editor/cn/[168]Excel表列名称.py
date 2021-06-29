# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。 
# 
#  例如： 
# 
#  
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：columnNumber = 1
# 输出："A"
#  
# 
#  示例 2： 
# 
#  
# 输入：columnNumber = 28
# 输出："AB"
#  
# 
#  示例 3： 
# 
#  
# 输入：columnNumber = 701
# 输出："ZY"
#  
# 
#  示例 4： 
# 
#  
# 输入：columnNumber = 2147483647
# 输出："FXSHRXW"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= columnNumber <= 231 - 1 
#  
#  Related Topics 数学 字符串 
#  👍 419 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            num = (columnNumber - 1) % 26 + 1
            ans.append(chr(num - 1 + ord("A")))
            columnNumber = (columnNumber - num) // 26
        return "".join(ans[::-1])
# leetcode submit region end(Prohibit modification and deletion)
