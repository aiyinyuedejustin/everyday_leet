#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (46.02%)
# Likes:    2660
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1], n = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1,2], n = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# 
# 进阶：你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #删除哪个，一定需要他之前的那个节点
        #因为要返回链表的头节点，需要一个虚拟节点
        dummy_head= ListNode(next=head)
        #需要一个fast指针移动n+1个单位，然后跟slow一起移动到fast=None.此时slow的下标刚好是要删除的元素的前一个
        slow, fast = dummy_head, dummy_head #一定要初始化为虚拟头，不然要删除第一个元素时，初始化为head就没用了。删除哪个一定需要他之前那个
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        

        slow.next= slow.next.next
        return dummy_head.next 

# @lc code=end

