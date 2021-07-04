# 给定一个化学式formula（作为字符串），返回每种原子的数量。 
# 
#  原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。 
# 
#  如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
#  
# 
#  两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。 
# 
#  一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。 
# 
#  给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数
# 量（如果数量大于 1），以此类推。 
# 
#  示例 1: 
# 
#  
# 输入: 
# formula = "H2O"
# 输出: "H2O"
# 解释: 
# 原子的数量是 {'H': 2, 'O': 1}。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# formula = "Mg(OH)2"
# 输出: "H2MgO2"
# 解释: 
# 原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
#  
# 
#  示例 3: 
# 
#  
# 输入: 
# formula = "K4(ON(SO3)2)2"
# 输出: "K4N2O14S4"
# 解释: 
# 原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#  
# 
#  注意: 
# 
#  
#  所有原子的第一个字母为大写，剩余字母都是小写。 
#  formula的长度在[1, 1000]之间。 
#  formula只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。 
#  
#  Related Topics 栈 哈希表 字符串 
#  👍 126 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedDict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        name_cnt_depth = []  # 名字-频率-括号深度
        stk = []  # 只存'(' 每到一处，左括号的个数就是当前name的深度
        i = 0
        while i < n:
            # --------------------------------（1）找名字
            name = ""
            if formula[i].isupper() == True:  # 大写字母开头
                name += formula[i]
                i += 1
            if name != '':  # 后面跟着小写字母
                while i < n and formula[i].islower() == True:
                    name += formula[i]
                    i += 1
            if name != '':  # 有名字！！！！！！
                # ------------------------------（2）这个名字的次数
                cnt = 0
                # ----如果name后面有数字
                if i < n and formula[i].isdigit() == True:
                    while i < n and formula[i].isdigit() == True:
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                    name_cnt_depth.append([name, cnt, len(stk)])
                # ----若name后面没数字
                else:
                    name_cnt_depth.append([name, 1, len(stk)])

            # --------------------------------（3）括号的情况
            if i < n and formula[i] == '(':
                stk.append('(')
                i += 1
            elif i < n and formula[i] == ')':
                i += 1
                cnt = 0
                # ----------后面有数字
                if i < n and formula[i].isdigit() == True:
                    while i < n and formula[i].isdigit() == True:
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                # ----------后面不是数字
                else:
                    cnt = 1

                # ------------------(4)')'后面的倍数
                for j in range(len(name_cnt_depth) - 1, -1, -1):
                    if name_cnt_depth[j][2] == len(stk):  # 是当前的深度
                        name_cnt_depth[j][1] *= cnt  # 字母复制
                        name_cnt_depth[j][2] -= 1  # 深度-1
                    else:
                        break
                stk.pop(-1)  # 当前深度的都计算好了，'('可以弹出了

        name_freq = SortedDict()
        for name, cnt, depth in name_cnt_depth:
            if name not in name_freq:
                name_freq[name] = 0
            name_freq[name] += cnt

        res = ""
        for name, freq in name_freq.items():
            res += name
            if freq > 1:
                res += str(freq)
        return res
# leetcode submit region end(Prohibit modification and deletion)
