# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。 
# 
#  请你返回字符串的能量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "leetcode"
# 输出：2
# 解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
#  
# 
#  示例 2： 
# 
#  输入：s = "abbcccddddeeeeedcba"
# 输出：5
# 解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
#  
# 
#  示例 3： 
# 
#  输入：s = "triplepillooooow"
# 输出：5
#  
# 
#  示例 4： 
# 
#  输入：s = "hooraaaaaaaaaaay"
# 输出：11
#  
# 
#  示例 5： 
# 
#  输入：s = "tourist"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母。 
#  
#  Related Topics 字符串 👍 33 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 1:
            return 0
        ans = 1
        preChar = s[0]
        maxLength = 1
        for i in range(1, len(s)):
            if preChar == s[i]:
                maxLength += 1
                continue

            ans = max(maxLength, ans)
            preChar = s[i]
            maxLength = 1
        return max(maxLength, ans)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    assert Solution().maxPower(s = "leetcode") == 2
    assert Solution().maxPower(s = "abbcccddddeeeeedcba") == 5
    assert Solution().maxPower(s = "triplepillooooow") == 5
    assert Solution().maxPower(s = "hooraaaaaaaaaaay") == 11
    assert Solution().maxPower(s = "tourist") == 1
