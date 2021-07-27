# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。 
# 
#  返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 输出：[7,4,1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
# 
# 
# 
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定的树是非空的。 
#  树上的每个结点都具有唯一的值 0 <= node.val <= 500 。 
#  目标结点 target 是树上的结点。 
#  0 <= K <= 1000. 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 307 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        h, f = {}, {}                       # h节点与深度的映射，f节点的父节点列表
        def g(r, i, fs):                    # r深搜树节点，i深度，fs该节点除自己以外的父节点列表
            if r:
                h[r.val] = i
                f[r.val] = [r.val] + fs     # 让最近的父节点排在最前面
                g(r.left, i + 1, f[r.val])
                g(r.right, i + 1 , f[r.val])
        g(root, 0, [])
        ans, ft, ht = [], set(f[target.val]), h[target.val] # ft目标节点的父节点哈希集合，方便存在判定，ht目标节点深度
        for i in h:
            for common in f[i]:             # 由近到远遍历目标点的父节点
                if common in ft:            # 如果存在共同父节点且满足条件
                    if ht + h[i] - 2 * h[common] == K:
                        ans += [i]          # 就加入答案
                    break
        return ans
# leetcode submit region end(Prohibit modification and deletion)
