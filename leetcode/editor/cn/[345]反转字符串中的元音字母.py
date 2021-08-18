# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入："hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  输入："leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  元音字母不包含字母 "y" 。 
#  
#  Related Topics 双指针 字符串 
#  👍 172 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        size = len(s)
        chars = list(s)
        l, r = 0, size - 1
        d = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while l < r:
            # print(l, r)
            if s[l] in d:
                while l < r:
                    # print(l, r)
                    if s[r] in d:
                        chars[l], chars[r] = chars[r], chars[l]
                        l += 1
                        r -= 1
                        break
                    r -= 1
            else:
                l += 1
        return "".join(chars)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    assert Solution().reverseVowels("leetcode") == "leotcede"
