# 输入一个字符串，打印出该字符串中字符的所有排列。 
# 
#  
# 
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 
# 
#  
# 
#  示例: 
# 
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
# 
#  
# 
#  限制： 
# 
#  1 <= s 的长度 <= 8 
#  Related Topics 回溯算法 
#  👍 294 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res_list = []
        self.cal(res_list, s, "")
        # print(len(res_list), res_list)
        return res_list

    def cal(self, res_list, chars, res):
        # print(res_list, chars, res)
        if len(chars) == 0:
            if res not in res_list:
                res_list.append(res)
            return
        for index in range(0, len(chars)):
            self.cal(res_list, chars[:index] + chars[index+1:], res + chars[index])
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation("aab"))
