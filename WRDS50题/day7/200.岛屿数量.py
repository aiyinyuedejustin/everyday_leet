#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode.cn/problems/number-of-islands/description/
#
# algorithms
# Medium (59.52%)
# Likes:    2334
# Dislikes: 0
# Total Accepted:    719.6K
# Total Submissions: 1.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #注意岛屿只能是上下左右相连的，斜着不算， 所以示例二的中间的1和左上角的1不算相连
        #dfs
        # 每次都是从一个1开始，然后把它周围的1都变成0，然后再找下一个1
        # 比如示例2.把左上角的全部吃掉，此时左上角全是0了，数量+1， 然后再找下一个1，也就是中间的1，然后右下角的1，数量+1

        # 用一个visited数组来记录是否访问过
        # 时间复杂度O(m*n)
        

        #版本2： 使用set 来记录
        # count = 0
        # #要看四个方向
        # directions = [(1,0),(-1,0),(0,1),(0,-1)] #上下左右
        # visited = set()
        # def set_island_zero(grid, r, c, some_set):
        #     #要先check boundary，然后再check是不是1
        #     if (0<= r < len(grid)) and (0<= c < len(grid[0])) and (r,c) not in visited and grid[r][c] == '1':
        #         visited.add((r,c))
        #         # grid[r][c] = '0' #当前的1变成0

        #         for row_inc, col_inc in directions:
        #             set_island_zero(grid, r+row_inc, c+col_inc, visited)
        
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == '1' and (row,col) not in visited: #找到一个1，就增加一个岛屿数量，然后把它周围的1都变成0
        #             count += 1
        #             set_island_zero(grid, row, col, visited)
    
        # return count


# O(m*n) 
# O(m*n) or O(1) if not counting the recursion stack
    


        # count = 0 

        # visited = set()
        # shangxiazuoyou = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # # need dfs
        # def change_to_zero(grid, row, col, someset):
        #     #
        #     #边界情况+ 如果是1 就add set （假设不能修改grid）
        #     if (0<= row <len(grid)) and (0<= col < len(grid[0]))\
        #           and (row, col) not in visited and grid[row][col] == '1':
        #         someset.add((row,col))
                
        #         #然后对于他的上下左右都继续dfs
        #         for row_increment, col_increment in shangxiazuoyou:

        #             change_to_zero(grid,row+row_increment, col+col_increment, someset)
                





        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):

        #         if grid[r][c] == '1' and (r,c) not in visited:
        #             count +=1 
        #             change_to_zero(grid, r, c, visited)
        # return count 





        count = 0

        visited = set()

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def turn_to_zero(somegrid, row, col, someset):

            if (0<=row < len(grid)) and  (0<=col < len(grid[0]))\
            and (row,col) not in someset and grid[row][col]=='1':
                someset.add((row,col))

                for row_inc, col_inc in directions:
                    turn_to_zero(somegrid,row+ row_inc, col+col_inc, someset)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count+=1
                    turn_to_zero(grid, r,c,visited )

        return count



        
# @lc code=end

