#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (58.95%)
# Likes:    1161
# Dislikes: 0
# Total Accepted:    224K
# Total Submissions: 379.7K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# 
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
# 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
# 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中结点数在范围 [0, 10^4] 内
# -1000 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # https://www.youtube.com/watch?v=u4JAi2JJhI8&ab_channel=NeetCode

    #1. serialize
    # taking an objext, put it into a readable string, that can be parsed easily
    # e.g. 123 Null Null 4 5 --注意这玩意后面还得转回去
    #可以用dfs, 简单一点 - pre order travasal 前序遍历： node-left-right


    # 对于 示例1 ， 序列化：
    # 前序遍历变成string ： '1, 2, null, null, 3, 4, null null，4,5 ‘
    # 解释：！！！！！
    # 首先1 然后左边2
    # 注意我们要加上2的左右两个子树表明 null 了。
    # 然后1 的右侧是3 ， 对于3 继续3的左右，是4；
    # 4 的左右是null null 。 然后5， 5的左右也是Null null 

    # 如何把  '1, 2, null, null, 3, 4, null null，4,5 ‘ 转化为 tree呢，反序列化：

    # 开始反向转化： 跟前序遍历一样，先建立left subtree走到头, then right subtree， recursively
    # 1 肯定是root ，
    # 先看1的left tree, 是2 :
            # 那么对于2， 继续看left tree 
            #       可以看出left 是null，左子树走到头了，done
            # 看2的right，
            #         还是null，所以2 的这个整个树完了
    # 然后看1的right tree，是3:
            # 那么对于3， 继续看left tree 
            #       可以看出left 是4，
            #           对于4继续看左边，null 左子树走到头了，
                        # 对于4 的右边还是 null， 右子树也走到头 done
            # 继续看3的right tree  是5
                        # 看5的left, right都是null， done
                   




    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #先用array 存储
        res = []

        def dfs(node):
            if not node: #base case
                res.append('N') #某个节点的左右节点都null了，我们用N代表
                return 
            res.append(str(node.val))
        
            dfs(node.left)#对于根节点的左右两侧都去执行这个，会不停的append 到res
            dfs(node.right)
            
        dfs(root)
        return ','.join(res) #用逗号连接起来，变成str
    

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')#用逗号，上面是用逗号隔开,变成一个list 【1,2,3,4,....】
        self.i = 0  # 也得是global的，下面还要recursive 用.用来表示目前val的index在哪

        def dfs(): #no param needed
            if vals[self.i] == 'N': #如果是N，我们就应该创建null node， base case
                self.i +=1  #we're done visiting this position, need to visit next one
                return None
            node =  TreeNode(int(vals[self.i])) #once create tree node for this positon

            self.i +=1 #still move on next one
            node.left = dfs() #是当前根节点的左节点，不用在+i，因为会recursively
            node.right = dfs()
            return node
        
        return dfs() #直接return就行了
    
# 都是O（n）
# "为了解决这个问题，我使用了深度优先搜索的方法。在序列化部分，我遍历了整个二叉树，
# 并将每个节点的值记录下来，包括空节点。我用特殊字符 'N' 表示空节点。
# 然后，我使用逗号将所有值连接起来，形成一个字符串。

# 在反序列化部分，我将字符串使用逗号分割，得到一个值的数组。然后，我使用深度优先搜索的方法，
# 根据数组中的值重新构建出二叉树。我使用一个全局索引来跟踪当前正在处理的值，这样我可以确保正确地为每个节点赋值。"





        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

