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
       #此处不能用dummy_head val=None,因为1最终指向的就是None，直接初始化pre为None即可，不然报错
       # 删： # dummy_head = ListNode(next=head,val =None) #初始化dummyhead，并且因为反转后1指向null，所以value=none
        cur , pre = head, None
        
        while cur:
            temp = cur.next# 先保存一下2，不然会断了
            cur.next = pre #让 1 指向none，此时1->2的链接断了
            pre = cur #先移动pre=1，在移动cur，不然cur动了，pre没法依赖
            cur = temp #移动cur往后一位


        
        return pre



# @lc code=end

