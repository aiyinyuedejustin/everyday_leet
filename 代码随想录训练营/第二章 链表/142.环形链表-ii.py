#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode.cn/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (57.56%)
# Likes:    2292
# Dislikes: 0
# Total Accepted:    736.1K
# Total Submissions: 1.3M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos
# 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 
# 不允许修改 链表。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目范围在范围 [0, 10^4] 内
# -10^5 <= Node.val <= 10^5
# pos 的值为 -1 或者链表中的一个有效索引
# 
# 
# 
# 
# 进阶：你是否可以使用 O(1) 空间解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # https://www.yuque.com/xiaoshan_wgo/alog/pcenhscg4tmx6ogz#tqtld
        #双指针判断是否有环
        #快指针每次走2个，慢指针每次1个。因此快指针每次相对慢指针走1个节点，一定能相遇。
        # 快指针肯定先进入环，

        fast = head
        slow = head

         #快指针一次2个，所以他的next也要判断不为空，这才是有环
        while fast and fast.next: 
            fast = fast.next.next # 如果链表没有环，fast 指针会首先到达链表的末尾，即 fast 或 fast.next 会变成 None。
            slow = slow.next

        # 在这种情况下，while fast and fast.next: 循环会停止，算法会返回 None，表示链表没有环。
         # If there is a cycle, the slow and fast pointers will eventually meet
          #相遇了
        
            if fast == slow:
                point1 = fast
                point2 = head
      # Move one of the pointers back to the start of the list
               #两个index
             
             #让他们每次都走一样的步长，最终再次相遇一定是入口处(x=z, 因此每次移动一样的步长，总会遇到的)
                  #一次走一步
                while point1 != point2:
                    point1 = point1.next
                    point2 = point2.next
                
                return point1
  
          
                  
             #已经是 入口处
        # If there is no cycle, return None
        return None
        
# @lc code=end

