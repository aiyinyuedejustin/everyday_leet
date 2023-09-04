#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode.cn/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (55.21%)
# Likes:    1323
# Dislikes: 0
# Total Accepted:    606.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [], val = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 列表中的节点数目在范围 [0, 10^4] 内
# 1 
# 0 
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #这个要用dummyhead, 因为可能删第一个元素，需要一个指向
        dummy_head = ListNode(next = head)
        current = dummy_head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:#注意这个else一定要写，也就是对于[1,2,2,3]来说，如果不写这个else，直接删除了2 后让current移动，那么就会错过第二个2
                current = current.next
        return dummy_head.next



# @lc code=end

