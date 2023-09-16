#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# https://leetcode.cn/problems/island-perimeter/description/
#
# algorithms
# Easy (69.97%)
# Likes:    696
# Dislikes: 0
# Total Accepted:    138.5K
# Total Submissions: 197.9K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。
# 
# 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# 输出：16
# 解释：它的周长是上面图片中的 16 个黄色的边
# 
# 示例 2：
# 
# 
# 输入：grid = [[1]]
# 输出：4
# 
# 
# 示例 3：
# 
# 
# 输入：grid = [[1,0]]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# row == grid.length
# col == grid[i].length
# 1 
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=_mQ_W4bMy6U&ab_channel=SaiAnishMalla
        # 答案是16
        #1. 先找到一个 assumed perimeter, 每次+4的周长。 一共有7个land， 因此4x7= 28
        #2. 找有多少个：connections（：two land share a side. （只找左侧和上侧的）--答案是6）
        # 如对于第二行第二列(1,1)的land，有4个side 。 但如果一次性算4个，
        # 那么（1,1）的左侧边和（1，0）的右侧边是一个，那就重复了
        # 因此我们每次只算左边 和 上边，这样就不会repitition. 这样对于每个land，
        # connextion的和是6（中间的黑边一共6）
        # 3. 在计算assumed perimeter的时候，其实有很多边被重复计算了，一共有6条边被重复计算了，
        # 就是我们connections的这6条
        # 3. 去除掉conenxtions: 28 - 6*2 = 16 ！！！

        len_row = len(grid) #多少行
        len_column = len(grid[0]) #多少列

        p = 0  #asummed perimeter
        connections = 0 #同样初始化

        for i in  range(0, len_row): #iterate  each row and column
            for j in range(0, len_column):
                if grid[i][j] ==1:#说明是land 
                    p += 4 #周长+4，

                    # check 顶端和左侧，为了找到connections
                    if i != 0 and grid[i-1][j]==1: # i !=0 是为了避免第一行，第一行上端没东西|
                        # grid[i-1][j]指something above me is land， 列是一样的
                        connections +=1 
                    # check最左侧，因为最左侧没connection， check我左侧，相同行的，是不是land
                    if j!=0 and grid[i][j-1] == 1:
                        connections+=1
        return p -(connections *2) # return




# @lc code=end

