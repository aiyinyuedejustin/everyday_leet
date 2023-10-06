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
        # #  虚拟头节点方式。定义一个dummy head指向原链表的头节点
        
        # dummy_head = ListNode(next = head) # 初始化一个虚拟节点，指向原链表的head，拼接原链表
        
      
        # current = dummy_head  # 定义临时指针current，一定要指向第一个，因为要删current next，所以cur一定是前面那个
        # # e.g. 如[dummy|next], [1|next],[2|next]， 要删除[1|next] ，记作cur next。那么cur应该是第一个，然后指向cur next next也就是[2|next]

        # # 遍历列表并删除值为val的节点
        # while current.next:# 只能用while，不然[1,1,1,1,1]的用if只能删一次，要持续删
        #     if current.next.val == val:# 如果下一个是要删的
        #         current.next = current.next.next# 指向后一个
        #     else:
        #         current = current.next #临时指针向后移 
        
        # return dummy_head.next

        # 自己写的：
        dummy = ListNode(next =head)

        pointer1 = dummy
        pointer2 = dummy.next

        while pointer2:
            if pointer2.val == val:
                pointer1.next = pointer2.next
                pointer2 = pointer1.next

            else:
                pointer1 = pointer1.next
                pointer2=pointer2.next
        
        return dummy.next
# @lc code=end

