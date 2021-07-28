# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。 
# 
#  如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记； 
# 
#  而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。 
# 
#  
# 
#  给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：label = 14
# 输出：[1,3,4,14]
#  
# 
#  示例 2： 
# 
#  输入：label = 26
# 输出：[1,2,6,10,26]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= label <= 10^6 
#  
#  Related Topics 树 数学 二叉树 
#  👍 83 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        depth = int( log(label) / log(2) ) + 1
        x = label
        res = []
        while x > 1 and depth > 1:
            res.insert(0, x)
            depth -= 1          #父节点的深度
            father_level_min = pow(2, depth - 1)
            father_level_max = pow(2, depth) - 1
            father = father_level_min + father_level_max - x // 2
            x = father
        res.insert(0, 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
