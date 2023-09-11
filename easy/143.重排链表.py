#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode.cn/problems/reorder-list/description/
#
# algorithms
# Medium (65.75%)
# Likes:    1370
# Dislikes: 0
# Total Accepted:    284.7K
# Total Submissions: 432.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# 请将其重新排列后变为：
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 
# 示例 2：
# 
# 
# 
# 
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
# 
# 
# 
# 提示：
# 
# 
# 链表的长度范围为 [1, 5 * 10^4]
# 1 <= node.val <= 1000
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # https://www.youtube.com/watch?v=S5bfdUTrKLM&ab_channel=NeetCode   ： 6:50
        ### 只是reorder，快慢指针-----eg[1,2,3,4]
        #先把链表中间cut分成2部分， 要先把第二部分的link反过来
        # 1. 
        #  慢指针指向1,速度1，快指针指向2，速度2。都向中间移动。

        #  如果是偶数个，当fast到最后的时候，slow就刚好是half的前一个：
        # eg：half在2、3之间，slow刚好在2：【1,2（slow）,3,4（fast）】

        # 如果是奇数个，[1,2,3,4,5],当fast 移动两次到5后面时，slow在3，那么firsthalf就是[1,2,3],secondhalf就是[4,5]
        #(视频6:50秒) 但这没事，每次先填firsthalf的第一个，second half reverse的第一个， 到最后填成了[1,5,2,4], firsthalf 还剩个3再填进去

        # 然后再次弄两个指针，指向1和5， 同时向中间移动直到相遇， 然后就是break link，所以要提前save一下temp value，跟之前链表 的题一样。
        # 注意最后一个node要指向null


        # #1. find middle 需要俩指针，指向1,2
        # slow , fast = head, head.next
        # while fast and fast.next: #如果是偶数个，fast停在最后一个，奇数个，fast还能执行一轮，停在null
        #     slow = slow.next #此时slow就在first half的最后一个
        #     fast = fast.next.next

        # # 2. reverse second half
        # second = slow.next #slow就在first half的最后一个，next就是第二部分的第一个 （指针1 
        # slow.next = None #因为要cut成两半，所以把第一部分的最后一个指向null，注意必须先执行上一行在这一行
        # prev = None #prev也是None，用于reverse第二部分 （指针2 ）

        # #距离奇数个，，second=slow.next =4,第二部分目前指针情况是[4(second)->5->null(prev)]

        # while second: #second是个指针，用于改变指向
             
        #     #！！背顺序！！先存second.next, 然后second.next移动指向到pre，然后移动pre到second，然后移动second= temp
        #     tmp = second.next #第一次存一下5 | 第二次存一下5.next =null
        #     second.next = prev # 移动指针，第一次让4->None | 第二次让5->4 
        #     prev = second # 然后先移动pre，在移动secondprev = 4 ， 第一次prev=4| 第二次prev=5 
        #     second = tmp # 第一次 second =5  |第二次second=null

        # # 至此为止[5(prev) -> 4->null(second)]
        
       
        # # merge two halfs.
        # # 重新定义两个指针，指向两个half的开头，然后依次填数
        # first = head
        # second = prev #prev是第二部分的开头了相当于，是5
        # while second:
        #     tmp1, tmp2 = first.next , second.next
        #     first.next =  #先更新first
        #     second.next = tmp1 #在更新second
        #     first, second = tmp1, tmp2 #两指针同时移动



#1, 找到一半
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        

#2，反转第二部分,定义cur 和pre两个指针
        cur = slow.next # [1,2,3(slow),4(cur),5->null]
        #断开第一部分
        slow.next = None
        #初始化pre=None
        pre= None

        while cur:
            tmp = cur.next#保存 tmp=5 | tmp=5.next=None
            cur.next = pre #更新指向 4-> None| 更新5->4
            pre = cur #移动pre到cur= 4 | pre到cur=5
            cur = tmp  #移动cur到tmp=5  | cur 到tmp=None
        #目前[5(pre)->4->null(cur)]
#3. merge两部分，重新定义两个指针
        first = head #1就是第一部分开头     [1->2->3->null]
        second = pre #5就是第二部分开头     [5(pre)->4->null]
        

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first , second = tmp1, tmp2 #最后一轮还剩下的first half的3，但他本身在上面就slow.next=null了所以不用管。












# @lc code=end

