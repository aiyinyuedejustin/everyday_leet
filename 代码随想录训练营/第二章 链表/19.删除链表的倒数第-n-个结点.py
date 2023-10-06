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
        # #删第n个，current指针一定是他前一个，然后让current指向n.next。那么n就被删除了
        # #继续虚拟头节点
        # #且要快慢指针

        # #定义fast指针和slow指针，初始值为虚拟头结点
        # # fast首先走n + 1步 ，为什么是n+1呢，因为只有这样同时移动的时候
        # # slow才能指向删除节点的上一个节点（方便做删除操作），如图
        # #fast和slow同时移动，直到fast指向末尾




        # dum_head = ListNode(next=head)

        # slow = dum_head
        # fast = dum_head

        # # 快指针比慢指针快 n+1 步
        # for i in range(n+1):
        #     fast = fast.next#走n+1次
        
        # # 移动两个指针，直到快速指针到达链表的末尾是null停止
        # while fast:
        #     slow = slow.next
        #     fast = fast.next
        
        # # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
        # slow.next = slow.next.next
        
        # return dum_head.next

        #快指针比慢指针先走n+1步
        # 同时从dummyhead 出发

        dummy = ListNode(next=head)
        fast = dummy
        slow = dummy

        for i in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
# @lc code=end

