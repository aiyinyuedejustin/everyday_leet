#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
# https://leetcode.cn/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (66.05%)
# Likes:    1243
# Dislikes: 0
# Total Accepted:    224K
# Total Submissions: 339.1K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random
# 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
# 
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random
# --> y 。
# 
# 返回复制链表的头节点。
# 
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# 
# 
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 
# 
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random 为 null 或指向链表中的节点。
# 
# 
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #hashmap + linkedlist
       #其实就是copy linkedlist，但是random指针指向的是随机的node，所以要用hashmap来记录新旧node的对应关系
        #所以要用hashmap来记录新旧node的对应关系
        #return head of copy linkedlist
        #直接看例子， copy后的linkedlist的random指针指向的是新的node，而不是旧的node但是长得一样


        # practice


        cur = head

        hashmap = {None:None}
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            hashmap[cur].next = hashmap[cur.next]
            hashmap[cur].random = hashmap[cur.random]
            cur = cur.next 




        return hashmap[head]

























        # dict1 = {None: None}
        # cur = head
        # while cur:
        #     dict1[cur] = Node(cur.val)
        #     cur = cur.next
        
        # cur = head
        # while cur:
        #     dict1[cur].next = dict1[cur.next]
        #     dict1[cur].random = dict1[cur.random]
        #     cur = cur.next
        
        # return dict1[head]


        # 思路：
        # hashmap存copy node的位置

        # 两次遍历：
        #     第一次： 遍历的node 复制node，存入hashmap，key和value都是node
        #     第二次： 把复制的node拿出来，然后给他的next和random赋值
        # 这样就复制完了，然后return head of copy linkedlist



        #这里的key是旧node，value是新node
        # node_map = {None:None}  # 这里为什么用普通字典而不用defaultdict呢？因为defaultdict的话，如果key不存在，会自动创建一个默认值，这里我们不需要这个功能
        # current = head

        # # 第一遍循环：复制节点，并记录新旧节点的对应关系
        # while current:
        #     node_map[current] = Node(current.val) #复制节点的值，并且变成新node，存入hashmap
        #     current = current.next #直到null

        # # 第二遍循环：复制 next 和 random 指针
        # current = head
        # while current: #这里的current是旧node, 
        #     #node_map[current]是新node， current.next是旧node的next， hashmap里面有每一个node所以currenct.next也在里面
        #     node_map[current].next = node_map[current.next] #把旧node的next指向的旧node的next对应的新node
        #     node_map[current].random = node_map[current.random] #同理，current.random是从原链表的random指针指向的旧node，node_map[current.random]是旧node对应的新node
        #     current = current.next #直到null

        # return node_map[head]

#TC O(n) 两次遍历
#SC O(n) hashmap存了n个node
# @lc code=end

