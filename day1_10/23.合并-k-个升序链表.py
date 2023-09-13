#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (58.33%)
# Likes:    2632
# Dislikes: 0
# Total Accepted:    704.1K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # https://www.youtube.com/watch?v=DvnxDGkjMDM&t=499s&ab_channel=CrackingFAANG
        # 每次把相邻两个list先相连 注意list整体没有删除元素!!!
        # 一次性只连 两个， 如一共6个，01 23,45 这样子先连，然后下一轮
        # merge其实是把后一个指针跟前面的屁股连起来。并不是删除original 的元素，而是连起来
        # 原始：[l0, l1, l2 , l3,l4,l5]
        # 第一轮： [l0->l1 ,l1, l2->l3, l3, l4->l5, l5] = [l0, l2, l4] 连接的时候，相邻index的间隔是1,注意list整体没有删除元素! L1虽然跟L0链接，但还在那
        # 第二轮 [l0->l2, l4] = [l0,l4] ,  连接的时候，相邻index的间隔是2(l0 l2) 注意list整体没有删除元素，这里省略了
        # 第三轮 [l0->l4] =result ,  连接的时候，相邻index的间隔是4(l0 l4)
        #观察到interval每次是*2 的关系 

        if not lists: #如果输入没东西，输出没东西
            return None

        interval =1 #interval总是从1开始，初始化
        while interval < len(lists): # interval总是比len小的，
            for i in range(0, len(lists)-interval, interval*2): #想merge every pairwise list| 
                # len(lists-interval) 不包含，每次上升两个，刚好到最后一个前一位，不管奇偶数个元素都可以
                lists[i] = self.merge(lists[i], lists[i+interval]) #相邻的两个 merge 注意list整体没有删除元素，第二轮依然是3个元素，只是取0,2为index

            interval *= 2 # interval *2,不是+2,为了skip over things
        return lists[0] #所有东西都merge完了，lists[0]就是排序好的，剩余位置不变，没有删除元素，直接return[0]
        
    def merge(self, l1, l2): #如何mer个相邻两个
        if not l1: #若list1 没东西，直接return list2
            return l2
        
        elif not l2: #相同
            return l1
        else: #开始merge
            if l1.val <= l2.val:
                l1.next = self.merge(l1.next, l2) #l1.next不仅仅是下一个节点的值，而是整个从那个节点开始的子链表
                return l1 #l1小，让l1后面的继续跟l2比较，并且保留当前l1
            else:
                l2.next = self.merge(l1, l2.next) #self.merge(l2.next, l1)用这个也行，merge进行下一层递归还是对称的，依然会判断val大小，只是这样写统一
                return l2
            
    
    #     if not lists:
    #         return None
        
    #     interval =1

    #     while interval< len(lists):
    #         for i in range(0, len(lists)-interval, interval*2):
    #             lists[i] = self.merge(lists[i], lists[i+interval]) #每一轮，后一个跟前一个连，但后一个还在那，lists总体元素数量不变

    #         interval *= 2
    #     return lists[0]
    # def merge(self, l1, l2):
    #     if not l1:
    #         return l2
    #     elif not l2:
    #         return l1
    #     else:
    #         if l1.val <= l2.val:
    #             l1.next = self.merge(l1.next, l2)
    #             return l1
    #         else: 
    #             l2.next = self.merge(l1, l2.next)
    #             return l2
    
# lists = [[1,4,5],[1,3,4],[2,6]]
# l1 = [1,4,5]
# l2 = [1,3,4]   
# 第一次调用 merge:

# l1.val (1) 和 l2.val (1) 相等。
# 我们选择l1的头部，并递归地合并l1.next和l2。
# 这时，我们再次调用merge函数，但这次是用[4,5]和[1,3,4]作为参数。
# 第二次调用 merge:

# l1.val (4) > l2.val (1)。
# 我们选择l2的头部，并递归地合并l1和l2.next。
# 这时，我们再次调用merge函数，但这次是用[4,5]和[3,4]作为参数。
# 第三次调用 merge:

# l1.val (4) > l2.val (3)。
# 我们选择l2的头部，并递归地合并l1和l2.next。
# 这时，我们再次调用merge函数，但这次是用[4,5]和[4]作为参数。
# 第四次调用 merge:

# l1.val (4) 和 l2.val (4) 相等。
# 我们选择l1的头部，并递归地合并l1.next和l2。
# 这时，我们再次调用merge函数，但这次是用[5]和[4]作为参数。
# 第五次调用 merge:

# l1.val (5) > l2.val (4)。
# 我们选择l2的头部，并递归地合并l1和l2.next。
# 这时，我们再次调用merge函数，但这次是用[5]和[]作为参数。
# 第六次调用 merge:

# l2是空的，所以我们只返回l1，即[5]。

# # 跳出merge：
# 第六次返回[5]- （l2空了，返回l1）
# 第五次返回[4,5] - l2.val = (4)
# 第四次返回[4,4,5] - l1.val =(4) 
# 第三次返回[3,4,4,5] - l2.val = (3)
# 第二次返回[1,3,4,4,5] - l2.val = (1)
# 第一次返回[1,1,3,4,4,5] - l1.val=  (1)
# 最终merge完毕就是list[i] 被填充为[1,1,3,4,4,5] ， list变成[ [1,1,3,4,4,5] ,[1,3,4],[2,6] ] ，注意list整体没有删除元素

#到了第二轮 ， 就merge，[1,1,3,4,4,5] 和[2,6]。lists并没有删除元素！！！



# @lc code=end

