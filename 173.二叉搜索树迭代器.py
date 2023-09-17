#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#
# https://leetcode.cn/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (81.62%)
# Likes:    707
# Dislikes: 0
# Total Accepted:    119.8K
# Total Submissions: 146.8K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
  '[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]'
#
# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# 
# 
# 
# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root
# 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
# int next()将指针向右移动，然后返回指针处的数字。
# 
# 
# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
# 
# 
# 
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next",
# "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# 输出
# [null, 3, 7, true, 9, true, 15, true, 20, false]
# 
# 解释
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // 返回 3
# bSTIterator.next();    // 返回 7
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 9
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 15
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 20
# bSTIterator.hasNext(); // 返回 False
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 10^5] 内
# 0 
# 最多调用 10^5 次 hasNext 和 next 操作
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以设计一个满足下述条件的解决方案吗？next() 和 hasNext() 操作均摊时间复杂度为 O(1) ，并使用 O(h) 内存。其中 h
# 是树的高度。
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
class BSTIterator:
    # https://www.youtube.com/watch?v=Q7ybpDST1n8&t=847s&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
    #in order中序： left - node - right
    # bst : 左小右大， in order 先走小的再走大的，先把左边走完，再走自己，再走右边
    # in oder走完后，拿出来本身就是sortted了
    #in order 走法:
    #1. intialize objext ,一路走到最左下，边走边存下node！
    #2. next（）被call的时候， 把list 最后pop出来--想成stack， last in first out,因为是顺序走的，
    # 刚刚走到最左下的时候，最后一个就是最小值所以next被call的时候，直接pop最后一个
    #3 因为 in order所以下一个node自然是node的右下， 这样整体左边走完了跑去右边，重复顺序这样一路走到右半边最左 （要给next做准备，才能给他最小值）因为bst的结构就是左小右大
    #5 return 刚pop出来的node给用户
    # hasnext， 直接看list长度是否大于0 -- 如果大于return True，不是说明没有，false

    # next / hasnext要O（1）的复杂度 ，memory是o(H) -- tree 高度



    #举例题目给的示例：（总是left-node-right)的顺序哦！！
    # 1. inital 的时候，有个[],把7加进去-> [7], 然后一路向左，边走边存node。看左下边-> [7,3]
    # 2. call 了next()， 把3拿出来，看3右边，由于3右边没东西， 直接return ->[7]
    # 3. call 了next()， 把7拿出来，->[] 看7右边， 由于7右边是15，加入list ->[15] 
    # 但由于要为下一次next做准备，要向左走到底，看15左边有9，9没有左边了->[15,9] 直接return 7  
    # 4. hasnext(), 长度不是0 ，True
    #5 next() , 应该吧9pop出，看9右边，没东西，直接return 9  ->[15] 
    # 6 hasnext() , 长度不是0 ，True
    # 7 , next(), 15 pop出来，->[] 看15右边， 是20
    #由于要为下一次做准备，看20左边，没有了， ，加入20 ->[20], 
    # 8. has next() -- True
    # 9. next() pop 20 ， 看20 右边，没了，直接return
    # 10 has next() --false， 因为->[]
    def __init__(self, root: Optional[TreeNode]):
       #题目给的是tree node
       self.stack = []
       while root: #一直向左看，直到左侧的头
          self.stack.append(root)
          root = root.left


    def next(self) -> int:
       return_node = self.stack.pop() #拿出来
       next_node = return_node.right #拿出来之后要看右边是否还有东西
       while next_node: #如果右边有东西，应该继续向左走到头，为下一次next()出来的最小值做准备（跟inital一样
          self.stack.append(next_node)
          next_node = next_node.left  #持续往左走


       return return_node.val#是val 哦


    def hasNext(self) -> bool:
       return len(self.stack) >0 #大于0自然是True
    
# TC: pop是O1, hasnext也是consta，虽然有遍历但， 平均是constant
# SC: O(h) 因为一路走到左下就是tree 高度



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

