# Write an efficient algorithm that searches for a value in an m x n matrix. Thi
# s matrix has the following properties: 
# 
#  
#  Integers in each row are sorted from left to right. 
#  The first integer of each row is greater than the last integer of the previou
# s row. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics Array Binary Search 
#  👍 3084 👎 194


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width, height = len(matrix), len(matrix[0])
        for row in matrix:
            if row[0] <= target <= row[height-1]:
                return self._contain(row, target)
        return False

    def _contain(self, data: List[int], target: int):
        for num in data:
            if num == target:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    assert Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
    assert not Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
