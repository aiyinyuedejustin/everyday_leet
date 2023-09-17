#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#
# https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (61.44%)
# Likes:    653
# Dislikes: 0
# Total Accepted:    54.4K
# Total Submissions: 88.5K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。
# 
# 返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。
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
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# 输出：[7,4,1]
# 解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1
# 
# 
# 示例 2:
# 
# 
# 输入: root = [1], target = 1, k = 3
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# 节点数在 [1, 500] 范围内
# 0 <= Node.val <= 500
# Node.val 中所有值 不同
# 目标结点 target 是树上的结点。
# 0 <= k <= 1000
# 
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # https://www.youtube.com/watch?v=pHdl1QOtf1g&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        #当成一个graph，以target 为中心，向外扩张k次， 
        # e.g 从5 向外扩张一次是362, 在扩张一次， 去除掉null，就是1 7 4 
        # 向外扩张 --- 一层层的向外 ---bfs
        # 要当成图，就要改成图：

            # 用hashmap把每一个节点的连接点记下 -- dict of list
            # dfs先遍历树，看有哪些连接点， ，对于每个点 格式是 ： [parent,左下， 右下]
            #eg  3:[5,1] (没有parent), 5:[2, 6,2], 1:[3, 0,8], 6: [5] (没有左右)

            #当然上面的这个node， 如3,5,1， 其实是当成key， ,value 就是list of [parent,左下， 右下]


        # 有了图之后 用bfs，从target开始扩张
        #用一个set， 看过的点就不用看了，直接跳
        #q 用来存储当前的节点和目前扩张到第几层， 这样每次pop都知道是谁和在第几层
        # 如果level = k， 就append 结果
        # 不然当前节点加到q， 更新level，继续bfs
    #return 结果、

        
#1. 定义转化graph函数（递归，也要找到最左下、最右下
        self.graph = defaultdict(list) # 用dict of list哦, 如{5:[2, 6,2], 1:[3, 0,8], 6: [5] (没有左右)}

        def make_graph(node,parent): #要填node和他的parent


            if not node: #找到最左下了，啥也没有
                return #return None
            
            # 用index标记当前节点, 按照parent， left， right顺序扔进去。
            #  如果任意一个是null，就是上面if node node, 直接None继续 ， 比如一直搜到最左，ndex 6: [5] (没有左右)
            if parent:
                self.graph[node].append(parent) #parent不用递归
            if node.left:
                self.graph[node].append(node.left) 
                make_graph(node.left, node) #对于左边继续recursive，左边的parent当然是当前node啦
            if node.right:
                self.graph[node].append(node.right)
                make_graph(node.right, node) #右边同样
#2. 开始转化graph
        make_graph(root,None) #因为root节点没有其他parent了

#3 准备bfs ， 需要visited， 还有q， 还有result列表
        visited = set()
        res = []
        q = deque() 
        #别忘了初始化
        q.append([target,0]) # 初始化q是 target 和当前扩张第几层。 由于target是5， 一开始扩张0次，所以[5,0]

        while q:
            node, level = q.popleft()
            if node in visited: #visite过了
                continue

            visited.add(node) #没有visit就加进去
            
            if level == k : #当前节点在q里面的level 已经是要的k了，那我们就找到了
                res.append(node.val) #val哦， 注意这个res会直到q空了才停止更新
            else:#不然要把连接点全部拿出来加入q， 并且level+1（已经向外扩张一次）
                for link in self.graph[node]: #看当前节点的[parent,left,right] 为了扩张出去
                    q.append([link,level +1]) #level+1 哦， 因为已经看过当前节点的三个连接点了
        
        return res


# on  
# on --- hashmap, call stack recursive 都是on 


        
        

        
# @lc code=end

