#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode.cn/problems/reverse-linked-list/description/
#
# algorithms
# Easy (73.62%)
# Likes:    3324
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2]
# 输出：[2,1]
# 
# 
# 示例 3：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目范围是 [0, 5000]
# -5000 
# 
# 
# 
# 
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
# 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #是单纯翻转，不是交叉反转哦

        ##第一次让1 指向None ，第二次让2 指向1， 最后return pre就是5 就是新的head

        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


# @lc code=end

