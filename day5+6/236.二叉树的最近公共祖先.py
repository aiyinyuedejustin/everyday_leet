#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (70.03%)
# Likes:    2448
# Dislikes: 0
# Total Accepted:    589.2K
# Total Submissions: 841.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [2, 10^5] 内。
# -10^9 
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://www.youtube.com/watch?v=pF_OeufBpOc&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        # lowest就是最上面的意思， 自己也可以是自己的祖先
        # eg1示例： 5,1 的output 是3， 因为5,1的祖先最往上是3
        # eg2示例： 5,4 的output 是4， 因为4在5的下面，5上面就没东西了，所以只能自己是自己的祖先，return 5
        # 额外示例: 1（root)-> 2 的output 是1， 因为1在2的上面，没东西了


        #注意题目给的提示：
        # all node.val are unique
        # p!=q
        # p and q will exist in the tree
        # node可以当自己的祖先

        #step : 用recursion 遍历树, 
        # 0 if not node return None
        # 1. 如果node是p or q，直接return，node，因为配对成功，自己可以是自己的祖先
        # 2. 不然就分成左右两边，去做recursion | left = self.xx(node.left, p,q )
        #3 。 如果左右都不是空，那return node, why? 因为要查最上面的相同祖先，比如示例1的 查到1, 5都不是空，那就return node =3 因为要往上面找
        #4 如果左边有东西，return 左，
        #  如果右边有东西return 右


        #对示例1 举例：
        # 首先看3， 不是p or q,
        # 先看左边是5， 刚好等于p，那么return node = 5. 再看右边是1， 刚好等于q， return node= 1
        # return 回去之后，看左右两边有没有东西 。那么对于3， 左右两边是5和1都不是空，那还是return node = 3， 那就找到了

        #对示例2 举例：
          # 首先看3， 不是p or q,
          # 看左边，5，是p，那么return当前node =5， left = 5
          # 看右边1，不是pq，那么继续看左右两边, 0 和 8 都不是p和q，直到null，已经无了，直接return null 回去
          #  所以对于1 ，左右两边都null， 那么1也是return null回去给3. 
          #那么对于3，左边是5， 右边是null， 根据第四步，左边有东西就reutrn 左边是5. 就找到了

        def dfs(node, p,q ):
        #edge case
            if not node: #停止条件
                return

            if node == p or node == q: #先看node是否是p or q，自己就是自己的祖先，直接结束
                # 通过在开始时加入这个 if 语句，可以更早地找到 p or q，并通过递归回溯来确定它们的最低共同祖先。这样做能提高算法的效率。
                return node
            
            #不然看左边和右边
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if left and right:  # recursion 结束后，如果左右两边都有东西，return node,然后继续往上找
                return node
            if left: #不然左边有东西就return 左边
                return left 
            if right: #右边有东西return 右边
                return right

        return dfs(root,p,q)
        


# On 每个点遍历一次
# On (recurssion 有call stack)





# @lc code=end

