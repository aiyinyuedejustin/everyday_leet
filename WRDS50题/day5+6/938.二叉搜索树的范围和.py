#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#
# https://leetcode.cn/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (82.12%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    123.9K
# Total Submissions: 150.9K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
# 
# 
# 示例 2：
# 
# 
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 2 * 10^4] 内
# 1 
# 1 
# 所有 Node.val 互不相同
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        
        # self.summ = 0
        

        # def dfs(node):
           
        #     if not node:
        #         return #停止，对self.summ无影响
        #         # 只有

        #     if low <= node.val <= high:
        #         self.summ += node.val
        #     if node.val > low :
        #         dfs(node.left)
        #     if node.val <high:
        #         dfs(node.right)
        # dfs(root)
        # return self.summ
            


        # https://www.youtube.com/watch?v=_GYF0mVvtYo&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        # bst的特性： 左小右大
        # 用dfs遍历每个点，
        # 把点的值那俩跟(low, high)比较
        # if low<= node.val <=high, 那符合条件加入total
        # 因为bst的特性，可以少遍历一些节点，比如 ：
        # only search when low< node.val <high,否则不查了(注意没有等号哦) 比如示例2的右侧15节点都已经=high=15了，再往下肯定比high大
        
         
        
        #方法1： recursive
        self.res = 0  #使用类属性
        # 累加满足条件的节点的值。当我们调用 recur 函数时，它会更新 self.res。这种方法允许我们跨多次递归调用保持和更新这个累加值。
        
        def recur(node):
            if not node: # 检查node是否为None 
                return #直接停
            
            if low <= node.val <= high:
                self.res += node.val
                
            if node.val < high:
                recur(node.right)
                
            if node.val > low:
                recur(node.left)
        
        recur(root) #update self.res
        return self.res


# o n 
# o n 

        # #方法2 ： 用stack， iterative，dfs
        
        res = 0 
        stack = [root]
        while stack:
            node = stack.pop() #一定是后进先出，LIFO，如果是pop(0)那就成了bfs
            if node:
                if node.val >= low and node.val<= high:
                    res+= node.val
                if node.val > low: #check当前node的value， 说明还能再小一点，往左看
                    stack.append(node.left)
                if node.val < high: #说明还可以再大一点，可以往右看
                    stack.append(node.right)

        return res

         
# @lc code=end

