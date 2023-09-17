#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode.cn/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (37.21%)
# Likes:    2159
# Dislikes: 0
# Total Accepted:    776.8K
# Total Submissions: 2.1M
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 
# 有效 二叉搜索树定义如下：
# 
# 
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,1,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # https://www.youtube.com/watch?v=hGrhoQVznMw&t=76s&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        #定义：
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

#重点: 用递归

# if root< left: False
# if root> right： False
    
# 
# 因为是tree的结构，需要左右开弓， 
#如果root 是空的，就跳过

# 方法1： recursive： 
        # base case: if root null, return True. 
        # +  not (root > left and root <right) return false
        # 最小最大先用-inf inf 代替
        # eg    3-  5 - 7 (5是头)
        # 对于5来说，check在不在lowest 和highest（-inf,inf), ok
        # 对于5的left和right： 
        # 先看3， 是不是在(-inf , 5)#左节点指定小于parent 
        # 再看3 的左右两边，都是null，直接可以return True

        # 再看7， 是不是在（5，inf）#右节点肯定大于上一个，
        #再看5的两个 子节点，都是null了，可以true

        #再回到5， 他的左右两侧的3和7都是true，那他也是true，那就完了


        return self.valid(root, float('-inf'),float('inf'))
    
    def valid(self, root, lowest, highest):
        if not root:# reach a null node, base case ， stop recursion, 这个点都没了，直接不判断了
            return True
        if not ( root.val > lowest and root.val < highest): # 括起来的就是我们想要的情况
            return False #如果不是就要false
        
        return self.valid(root.left,lowest,root.val) and self.valid(root.right,root.val,highest) #这两个要同时满足，chekc

        #self.valid(root.left,lowest,root.val)： every on the left have to be less than parent,所以highest填root。val
        #self.valid(root.right,root.val,highest) ，  every on the right have to be greater than parent, 所以lowsest 填 root.val

# o n
# o n
# @lc code=end

