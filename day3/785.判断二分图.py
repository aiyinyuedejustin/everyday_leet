#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# https://leetcode.cn/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (54.82%)
# Likes:    482
# Dislikes: 0
# Total Accepted:    81.9K
# Total Submissions: 149.3K
# Testcase Example:  '[[1,2,3],[0,2],[0,1,3],[0,2]]'
#
# 存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。给你一个二维数组 graph ，其中
# graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v
# 之间的无向边。该无向图同时具有以下属性：
# 
# 不存在自环（graph[u] 不包含 u）。
# 不存在平行边（graph[u] 不包含重复值）。
# 如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
# 这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
# 
# 
# 二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B
# 集合，就将这个图称为 二分图 。
# 
# 如果图是二分图，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# 输出：false
# 解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。
# 
# 示例 2：
# 
# 
# 输入：graph = [[1,3],[0,2],[1,3],[0,2]]
# 输出：true
# 解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。
# 
# 
# 
# 提示：
# 
# 
# graph.length == n
# 1 
# 0 
# 0 
# graph[u] 不会包含 u
# graph[u] 的所有值 互不相同
# 如果 graph[u] 包含 v，那么 graph[v] 也会包含 u
# 
# 
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # https://www.youtube.com/watch?v=mev55LTubBY&ab_channel=NeetCodeIO

        # any node cannot be in the same set as its neibours 
        
        #把两个set 叫做odd 和even

         #对于图1： 0 的邻居是123，  先把0 放在 even，再把123放在odd 
        # |odd   | even|
        # | 1,2,3| 0   |
        # |      |     |
      
        #检查： 对于3， 他的左邻居0在even，不在同一个set。但是右邻居2跟他在同一个set，这就不行

        #对于图2： 0 的邻居是13，  先把0 放在 even，再把13放在odd 。又检查2，同样13都在odd。都没问题。因此可以分成[1,3] [0,2]
        # |odd   | even|
        # | 1,3   | 0   |
        # |   1,3 |  2   | 

        #其实就是说，对于一个在odd set里面的node 他的邻居只能在even set。 这就是bipartite的意思



        odd = [0] * len(graph) # graph里面有几个node就初始化几个， 0 代表还没visit过
        # 要！！！map node i to odd =1 and even = -1
        

        def bfs(i): #i 指的是starting point，也就是index，也就代表每个node
            if odd[i]: #对应下面的for loop ， 如果某个node已经visit过，其实就存在odd里了，所以odd[i]就不是0 
                return True #这里不是真的true的意思其实只是stop当前这个 node的search
            
            q = deque([i])   # initial i in q
            odd[i] = -1 #初始化i for even set

            while q: #q 
                i = q.popleft() 
                for nei in graph[i]: #对于每个node的neighbour，用当前node的index取出来[1,2,3]
                    if odd[i] == odd[nei]: #当前节点和他nei的值一样，
                        return False # 说明在同一个set里了，直接false， not bipartite
                    elif not odd[nei]: #only nei it's not visitied we'll revise， 对应上面if odd[i]: return True
                        q.append(nei)
                        odd[nei] = -1 *odd[i] #让所有nei的值(分类) 都跟i 反着
                    #注意这里不是else

            return True #while 完了检查完了return true
        
        for i in range(len(graph)): #注意graph might not be connected链接起来，所以要对每个starting point都run bfs
            if not bfs(i): #if not bipartite for any starting point
                return False
        
        #循环完了也没false说明可以bipartite
        return True

            




# @lc code=end

