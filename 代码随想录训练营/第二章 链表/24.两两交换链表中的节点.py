#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (71.66%)
# Likes:    2004
# Dislikes: 0
# Total Accepted:    698.6K
# Total Submissions: 974.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None #[]
        
        dummy = ListNode(next=head)
        
        current = dummy

        while current.next and current.next.next:
            temp1= current.next
            temp2 = current.next.next.next

            current.next = current.next.next #让dummy->2，此时dummy->已经断了 | 1->4
            #让2 指向1 
            current.next.next = temp1  # ||4->3
            #让1指向3 
            temp1.next= temp2 #3-》null
        
            #移动指针
            current = current.next.next # 此时指向1，开始下一轮循环。此时 dummy->2->1->3->4->null
        return dummy.next

# @lc code=end

