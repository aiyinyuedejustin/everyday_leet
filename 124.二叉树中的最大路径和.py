#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (45.30%)
# Likes:    2053
# Dislikes: 0
# Total Accepted:    344.9K
# Total Submissions: 761.2K
# Testcase Example:  '[1,2,3]'
#
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
# 节点，且不一定经过根节点。
# 
# 路径和 是路径中各节点值的总和。
# 
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 
# 示例 2：
# 
# 
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000 <= Node.val <= 1000
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        #跟 543 一样， 只不过那个少一些步骤，只需要路径长度-- 
        # https://www.youtube.com/watch?v=47fPVmNqaxQ&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        #且不一定经过根节点 -- 示例二，最大路径和就是右下角三角
        # 注意如果我们要照顾好左右节点，比如我们选了20作为root，那就没法往上走了，只能用左右两边的
        # 因为（同一个节点在一条路径序列中 至多出现一次 ），只能走一次

        #用dfs 一路走到最左边，然后往回计算,recursive:
        # 需要建立一个 non-local的variable 存储最大值 - self.max_
            # # base case: 如果当前空， return 0--不是return None，因为最后要一个sum（算到最后最下面没点了就是return回去0）
            # recursive 算左也算右，
            #       note：因为是要最大，所以如果算出来的值是负的，就让他等于0  ！！
            # 计算目前点的总和--目前三角形的

            # 更新目前最大值->max(current,new)--non local,因为不停recursive互相叫

        #     return当前路径最大值指的是node+left/right。然后继续recursive回去往上走，为了看往回走还有没有加起来更大的
        #           --注意，对于某个root，要看左边大还是右边大，那边大用哪个，current+left/right
        
        # call dfs， 计算最大总和
        # 最后return 最大路径综合

        #non -local 
        self.max_ = float('-inf') #不管第一次是啥，都可以取代-inf。 如果只有一个node=-3, 结果就是-3，如果初始化为0，那会最终return 0，就不对了
        
        def dfs(node):
            if not node:
                return 0 #base case
            
            #算左右两边的和
            left = max(dfs(node.left) ,0) # 注意持续找下去可能变成负数，我们只要0，不是上面if not node代替得了的
            right = max(dfs(node.right) ,0)#同样算right

            #目前三角形的最大值，
            cur_path_sum = node.val + left +right #left right已经是数字了，当前节点还不是/这玩意可能是
            
            #我们要找到路径最大总和，要用non-local因为要共享，max累积
            self.max_ = max(self.max_, cur_path_sum)

            return max(left,right) + node.val #return是要最大的那条，看左右那边大.
             # 这一步是为了sum某一边然后跟上面连起来继续sum，而不是当前三角形的sum


        dfs(root)
        return self.max_

# "为了找到二叉树中的最大路径和，我使用了深度优先搜索的方法。从底部开始，
# 对于每个节点，我都计算了通过该节点的最大路径和，同时还计算了包括该节点及其左右子节点的路径总和。
# 然后，我用这个路径总和更新了全局的最大路径和。这个算法确保了我们能够考虑所有可能的路径，
# 并找到具有最大总和的路径。


# 我们可以使用递归的方式，从底部开始，对每个节点，我们都计算通过该节点的最大路径和。
# 这个“通过”是指选择了这个节点，并可能选择它的左或右子节点，但不会同时选择两者。

# 对于每个节点，有两个选择：

# 包含该节点和它的左子节点的最大路径。
# 包含该节点和它的右子节点的最大路径。
# 同时，对于当前节点，我们还会计算包括它及其左右子节点的路径总和（形成一个"三角形"的路径），
# 并更新我们的全局最大路径和。

# 初始化一个全局变量 self.max_ 为负无穷大。这是为了确保在所有情况下，即使所有节点都是负数，我们也能找到一个最大值。

# 定义一个递归函数 dfs(node)。这个函数会返回通过当前节点的最大路径和。

# 在递归函数中，首先处理基本情况：如果节点不存在，返回0。

# 递归计算该节点左子树和右子树的最大路径和。这里，我们确保路径和永远不是负数。如果是负数，我们直接返回0，因为负数会降低路径的总和。

# 计算当前节点的“三角形”路径和，即 node.val + left + right。

# 更新全局的最大路径和 self.max_。

# 返回该节点的最大路径和，即 max(left, right) + node.val。

# 最后，对根节点调用 dfs(root) 并返回 self.max_。



# TC: O(N) 每个点只有一次
# SC: O(N) count recursive stack space 


# @lc code=end

