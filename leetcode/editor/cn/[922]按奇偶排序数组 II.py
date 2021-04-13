# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。 
# 
#  对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。 
# 
#  你可以返回任何满足上述条件的数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 20000 
#  A.length % 2 == 0 
#  0 <= A[i] <= 1000 
#  
# 
#  
#  Related Topics 排序 数组 
#  👍 125 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        index = 0
        while index < len(A):
            flag = index % 2
            if A[index] % 2 != flag:
                for i in range(index+1, len(A)):
                    if A[i] % 2 == flag:
                        A[index], A[i] = A[i], A[index]
                        break
            index += 1
        return A

        
# leetcode submit region end(Prohibit modification and deletion)
