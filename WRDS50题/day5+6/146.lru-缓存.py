#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
# https://leetcode.cn/problems/lru-cache/description/
#
# algorithms
# Medium (53.47%)
# Likes:    2856
# Dislikes: 0
# Total Accepted:    523.2K
# Total Submissions: 978.4K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 
# 实现 LRUCache 类：
# 
# 
# 
# 
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 
# 
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
# 
# 
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10000
# 0 <= value <= 10^5
# 最多调用 2 * 10^5 次 get 和 put
# 
# 
#

# @lc code=start




   #capacity 是max 几个，如2 ，就只能存2个
    # 如果抄了capaty，要删除最没用过的关键字
    # 用一个left 表示least recent， right表示most recent
    # 什么时候get 了(1,1) 那么(1,1 )就是最近用的， (2,2)变成了不用的，会交换顺序
     #交换顺序就需要一个double linked list

    # (1, 1) 是 （key， value） or （node， value
    #get put 要O(1)， 用hashmap。 key应该是这个node, value应该是pointer to node , (1key, 1(point to this))



    #当目前已经有2个，要加入一个（3，3）时，应该更新left 为(1,1), right(most recent) 就成了(3,3), 
    # 还要更新hashp map的key to be 3 /value to new node 3


    #总结: 1. 一个hashmap， key是same key from input, value是 pointer to node
    # 2. 一个double linked list自己写个class, 每个node都有prev 和next两个pointer， 每个都是node 
    # 3. left right 是dummy node，指向最不常用，和常用的。 left.next永远是lru， right.prev是most recent


# class Node: #需要额外创建个doulbe linked list（额外添加
#    def __init__(self, key, val):
#       self.key , self.val = key, val #node自己也有key
#       self.prev = self.next = None #inital None
      

# class LRUCache:
 


#     def __init__(self, capacity: int):
       
#        self.cap = capacity
#        self.cashe = {} #hashmap --- map key to node
#         #left: least recent , right: most recent
#        self.left , self.right = Node(0,0), Node(0,0) #需要个dummy，用0 initiallize
      
#        #want these know to initally connect to each other,如果要put一个新node，要put between left right
#        self.left.next, self.right.prev = self.right, self.left

#        # left-><-right 现在长这样

#     def remove(self, node): #remove node from list(额外的helper)
#        # 需要当前node的前一个和后一个，然后前一个指向后一个，后一个指向前一个，中间就无了
#        prev, nxt = node.prev, node.next
#        prev.next , nxt.prev = nxt, prev
       
    
#     def insert(self, node): #insert at right（额外的helper)因为每次right都是最新的most recent
#        # [1]-><-right 原来这样，要在这俩之前插入，那么就是[1]-><-【new】-><-right
#        # 【new]的上一个是原先right的上一个， 新节点的下一个就是right
#        prev, nxt = self.right.prev, self.right
#         # [1]的下一个是[new] ， right的上一个也是[new]
#        prev.next = nxt.prev = node
#        # [new]的上一个是[1], 下一个是right
#        node.prev = prev
#        node.next = nxt
       


#     def get(self, key: int) -> int:
        
#         if key in self.cashe: #有
#           self.remove(self.cashe[key]) #先remove 
#           self.insert(self.cashe[key]) #再insert，这样就swap到right，就成了最新的那个
#           return self.cashe[key].val 
#           # 由于cashe的value其实是pointer to node, 
#           # 所以self.cashe[key]拿到的是node，然后还要node.val
#         return -1 #如果没找到
       


#     def put(self, key: int, value: int) -> None:
#         if key in self.cashe: #说明node already exist，且same key-value,其实是想remove后更新
#            self.remove(self.cashe[key]) #remove之前的
#         self.cashe[key] = Node(key,value) #更新,现在hash map 有了一个pointer to new node
#         self.insert(self.cashe[key]) #但还要insert into list，self.cashe[key] 拿出来的就是这个node 

#         #insert后要检查长度，长了的话让上一个不常用的作废
#         if len(self.cashe) > self.cap:
#            #remove least recent
#            lru = self.left.next #left的next就是 , lru指一个node
#            self.remove(lru) #remove from linked list
#            del self.cashe[lru.key]#del key from hash map. lru是node， node有key这个属性（看下面定义），跟hashmap里面的key相同
           
       

# 简便写法： order dict。每次更新移动到后面
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
      #   初始化一个具有给定容量 capacity 的 LRU 缓存。self.cache 是一个 OrderedDict，
      # 用于存储缓存项。OrderedDict 会记住元素添加的顺序。

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
#     如果 key 不在缓存中，返回 -1。
# 如果 key 在缓存中，使用 move_to_end() 方法将其移到有序字典的末尾。
# 这样，最近使用的项就会在 OrderedDict 的末尾，而最近最少使用的项在开始处。
# 返回 key 对应的值

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

#             如果 key 已经在缓存中，使用 move_to_end() 方法将其移到有序字典的末尾。
# 无论 key 是否已经在缓存中，都将其值设置或更新为 value。
# 如果缓存的大小超过了 capacity，则使用 popitem(last=False) 删除最早添加的（即最近最少使用的）项。
# 这个实现使得 get 和 put 操作都具有 O1的时间复杂度。


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

