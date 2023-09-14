#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
# https://leetcode.cn/problems/clone-graph/description/
#
# algorithms
# Medium (69.22%)
# Likes:    640
# Dislikes: 0
# Total Accepted:    123.1K
# Total Submissions: 177.8K
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
# 
# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
# 
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
# 
# 
# 
# 测试用例格式：
# 
# 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val =
# 2），以此类推。该图在测试用例中使用邻接列表表示。
# 
# 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
# 
# 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
# 输出：[[2,4],[1,3],[2,4],[1,3]]
# 解释：
# 图中有 4 个节点。
# 节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
# 节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
# 节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
# 节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：adjList = [[]]
# 输出：[[]]
# 解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
# 
# 
# 示例 3：
# 
# 输入：adjList = []
# 输出：[]
# 解释：这个图是空的，它不含任何节点。
# 
# 
# 示例 4：
# 
# 
# 
# 输入：adjList = [[2],[1]]
# 输出：[[2],[1]]
# 
# 
# 
# 提示：
# 
# 
# 节点数不超过 100 。
# 每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
# 无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
# 由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
# 图是连通图，你可以从给定节点访问到所有节点。
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # https://www.youtube.com/watch?v=mQeF6bN8hMk&ab_channel=NeetCode
        # a connected undirected(goes both way) graph.
        # want excact value, but new graph 


        # use hash map

        #正着链接一遍，剩一个节点没有双向链接。 那就从最后一个节点反着再来一遍，就能把1和3

        # 1、 添加1 ，check neighbour, 应该有个2，但hashmap里还没有，添加2，then 1-> 2
        # 2. for 2  ，check neichbour, 应该有个1 and 3，hashmap里有1 没3， 添加3 ，then 1<->2->3 
        # 3. for 3  ，check neichbour, 应该有个2 and 4，hashmap里有2 没4， 添加4 ，then 1<->2<->3->4
        # 4. for 4  ，check neichbour, 应该有个1 and 3，hashmap里有1 有3， then1<->2<->3<->4->
        # 5。然鹅1还没跟4链接，从4开始 反着再来一遍，就能把1<->4


        oldToNew = {} #hash map

        def dfs(node):
            if node in oldToNew: #if it's in hashmap, we've already cloned
                return oldToNew[node] # just return , no double-check

            copy = Node(node.val) #make a clone | val 属性被设置为 node.val| neighbors 属性被初始化为空列表
            
#             class Node {  #就用这个，创建一个Node对象
#     public int val;
#     public List<Node> neighbors;
# }
            oldToNew[node] = copy # add to hashmap ，后面没用，只是
            for nei in node.neighbors: #go through neighbors of original node
                copy.neighbors.append(dfs(nei)) #run dfs on nei, 会跳到开头，return oldToNeW[nei]。
                # clone neighbour recursively
            return copy

        return dfs(node) if node else None #一开始给你的node可能是null---adjList = [[]]
        
# @lc code=end

