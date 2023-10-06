#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode.cn/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (58.94%)
# Likes:    1406
# Dislikes: 0
# Total Accepted:    345.6K
# Total Submissions: 586.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你一棵二叉树的根节点，返回该树的 直径 。
# 
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
# 
# 两节点之间路径的 长度 由它们之间边数表示。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 10^4] 内
# -100 <= Node.val <= 100
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         #跟 124 一样， 只不过那个多一些步骤，也是各自计算目前三角形，和左右两侧传导的max那条路径

        #https://www.youtube.com/watch?v=irxdNPqxpxM&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        #最长路径的一半 --- 可能不用经过根节点
        #1. 找出左边的最长， 和右边的最长(diamiter)
        # 2. 用dfs 找  （递归
        # 2.1 如果是空节点，return 0 -- base case
        #3. left right 各自递归调用，
        #4 self.diam 跟 left+right比较（
        # 3.  每次找到最左  最右的时候跟目前 diamiter比较，（用max）-- left right都是俩调用dfs
        # 4. 找到底部，就return找到的最长值（ 左右两边哪个长） + 当前的点
        #         类似之前有一题的bfs最长路径和那个，
        #         1 + max（left,right)
        
        # return 最终的额dimater


        self.diam =  float('-inf')


        def dfs(root):

            if not root: #找到底部。左右两边都是null，return 0 。不能return None因为是要lenght of path
                return 0 
            


            left = dfs(root.left)
            right = dfs(root.right)

            
            self.diam = max(self.diam, left+right ) #当前三角形的最长路径

     
            #目前node，从左边往自己走， 还是从右边往自己走，哪个大， 要加上自己的长度为1 
            return  1+max(left,right)  #目前node，从左边走or从右边走哪边最大，为了传导给上面递归reutnr回去
            #想象走到4的下面的时候1+ max (0,0) 你只能return 一个1 给2 ， 5也是return一个1给2. 
            # 那么下一轮对于2这个三角形的 总长度就是max(self.diam, 1+1) =2，是对的
        dfs(root)
        return self.diam
    
# tc: o n
# sc: o h --- 用了一个call stack 就是 o h -- 如果最左走到底， 那就用了树高度的
# @lc code=end

