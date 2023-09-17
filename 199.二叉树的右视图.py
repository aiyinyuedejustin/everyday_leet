#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode.cn/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (66.06%)
# Likes:    945
# Dislikes: 0
# Total Accepted:    317.9K
# Total Submissions: 480.8K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 
# 
# 示例 2:
# 
# 
# 输入: [1,null,3]
# 输出: [1,3]
# 
# 
# 示例 3:
# 
# 
# 输入: []
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# 二叉树的节点个数的范围是 [0,100]
# -100  
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        #base case 肯定是
        if not root:
            return []
    
        #用bfs, q + popleft()
        q = deque([root])
        res = []

        while q:
            level_length = len(q) # only iterave current level ,所以需要一个len

            for i in range(level_length): #only process on that level
                node = q.popleft()
                if not node: #其实可以不要，前面根节点已经检查了非空if not root:。 后面对于root的剩余任何left right
                                            # 也都是不空的时候才append，所以这个没必要
                    continue

                if i == level_length -1:
                    res.append(node.val) #到了这个level的最后一个的时候就是最右侧的
                if node.left: #左侧有东西（下一层的）就加进去，这样下一层可以继续搜索
                    # 如果我们不将左右子节点加入队列，我们就无法访问和遍历树的下一层，也就无法找到每一层的最右侧节点。
                    # 因此，if node.left: q.append(node.left) 和 if node.right: q.append(node.right) 
                    # 这两行代码确保了我们能够遍历整棵树并找到每一层的最右侧节点。
                    
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res



# @lc code=end

