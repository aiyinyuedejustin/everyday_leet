#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode.cn/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (72.30%)
# Likes:    1140
# Dislikes: 0
# Total Accepted:    347.4K
# Total Submissions: 480.7K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 边界（四个角）最关键。使用左闭右开。转圈数=n/2，如果是奇数，最后中间的位置单独考虑o
        # start_x , start_y = 0,0

        # count = 1 
        # loop = n//2 # 不同大小所需圈数
        # center = n//2 #如果n是奇数，中心店为[center,center]
        # array = [[0] * n for _ in range(n)] #初始化

        # for offset in range(1, loop +1):
        #     #e.g 3x3的矩阵
        #     for y in range(start_y, n-offset): #行：0，列：0， 1
        #         array[start_x][y] = count #从0行开始，留出最后一位
        #         count +=1 

        #     for x in range(start_x,n-offset): #行：0,1， 列：2
        #         array[x][n-offset] =count
        #         count +=1

        #     for y in range(n-offset,start_y,-1):#行：2，列：2,1
        #         array[n-offset][y] = count
        #         count +=1
        #     for x in range(n-offset,start_x,-1) :#行：2,1 列：0
        #         array[x][start_y] = count
        #         count +=1

        #     start_x +=1 #做完第一圈，index往里一个
        #     start_y +=1


        # if n % 2 ==1: #奇数直接填充中心店
        #     array[center][center] = count#count在上一次循环已经加到最后一位了
        # return array

        center = n //2

        loop = n//2

        startx, starty = 0,0

        count = 1
        res = [  [0]*n for _ in range(n)]
        for offset in range(1,loop+1): #1

            for y in range(starty, n - offset):
                res[startx][y] = count
                count +=1
            for x in range(startx, n-offset):
                res[x][n-offset]= count
                count +=1
            for y in range(n-offset, starty,-1):
                res[n-offset][y] = count
                count+=1
            for x in range(n-offset,startx,-1):
                res[x][starty] = count
                count +=1
            
            startx = startx +1
            starty = starty+1

        if n % 2 ==1:
            res[center][center] = count
        return res


# @lc code=end

