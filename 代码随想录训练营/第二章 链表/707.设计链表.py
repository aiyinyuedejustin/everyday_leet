#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#
# https://leetcode.cn/problems/design-linked-list/description/
#
# algorithms
# Medium (34.58%)
# Likes:    918
# Dislikes: 0
# Total Accepted:    252.5K
# Total Submissions: 730.6K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
  # '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# 你可以选择使用单链表或者双链表，设计并实现自己的链表。
# 
# 单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。
# 
# 如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。
# 
# 实现 MyLinkedList 类：
# 
# 
# MyLinkedList() 初始化 MyLinkedList 对象。
# int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
# void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
# void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
# void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果
# index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
# void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# 输出
# [null, null, null, null, 2, null, 3]
# 
# 解释
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
# myLinkedList.get(1);              // 返回 2
# myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
# myLinkedList.get(1);              // 返回 3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= index, val <= 1000
# 请不要使用内置的 LinkedList 库。
# 调用 get、addAtHead、addAtTail、addAtIndex 和 deleteAtIndex 的次数不超过 2000 。
# 
# 
#

# @lc code=start
class MyLinkedList:


    def __init__(self):
       self.dummy_head = ListNode()#自己的属性，先不填next=什么，因为一开始是空的，
       self.size = 0#初始化为0


    def get(self, index: int) -> int:
        # 如果目前是[10,11,12,13]
      if index < 0 or index > (self.size-1): #index必须要合法，从0开始且不能超过index长度范围
          return -1 #如果下标无效，则返回 -1 。
      cur = self.dummy_head
      for i in range(index+1):
        cur = cur.next
      return cur.val#定要加val！！！



    def addAtHead(self, val: int) -> None:
      new_node = ListNode(val)
      #先链接后边，再链接前面，最好这样以防出错
      new_node.next = self.dummy_head.next #在开头加，因此永远follow dummy的下一个是新节点的下一个
      self.dummy_head.next = new_node
      self.size +=1 #记得加1，一开始是空的



    def addAtTail(self, val: int) -> None:
      new_node = ListNode(val)
      #需要一个指针,指向dummyhead
      cur = self.dummy_head
      while cur.next:#最后一位的next是none时，说明指针到了最后一位
        cur =cur.next
      cur.next =new_node
      self.size +=1  #记得加1，一开始是空的




    def addAtIndex(self, index: int, val: int) -> None:
      #n必须要合法，从0开始。如果目前是[10,11,12,13]+new
      # index操控指针走的步数，若要在13后添加一个，从dummyhead最多走4步也就是size=4.所以n 不能大于self.size
      if index < 0 or index > self.size :
        return #直接停止
      cur = self.dummy_head
      new_node= ListNode(val)
      for i in range(index): #如在index=4插入，从dummyhead移动4次就到了13
        cur = cur.next 
      new_node.next = cur.next #如果要在index3加入一个，一定要先让新节点连接后一个，也就是之前的13，不然就有头无尾
      cur.next =new_node
      self.size +=1

  
    def deleteAtIndex(self, index: int) -> None:
      if index < 0 or index > (self.size -1):#判断下标有效
        # 如果目前是[10,11,12,13], 最多index到3，也就是size-1
        return 
      cur = self.dummy_head
      for i in range(index):
        cur = cur.next #移动到要delete的前一个。如delete 11,cur就从dummyhead移动到10
      cur.next =cur.next.next#删除
      self.size -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

