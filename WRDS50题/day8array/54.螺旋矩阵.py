#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (49.77%)
# Likes:    1517
# Dislikes: 0
# Total Accepted:    420.1K
# Total Submissions: 844.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # res = []
        # top, down = 0, len(matrix)-1#down是行数
        # left, right = 0, len(matrix[0]) -1 #right 就是列数

        # while top <= down and left <= right :

        #     for i in range(left,right+1 ): #0,1,2 列数
        #         res.append( matrix[top][i])
        #     #第一行结束了, 指针移动到第二行, 1
        #     top +=1  #top =1 


        #     for i in range(top, down+1):#行数，# return 1,2 
        #         res.append(matrix[i][right])
        #     right -=1 #最后一列结束了往左移动, 1

        #     if top <= down : #最后还剩个5的时候免得list out bound
            
        #         for i in range(right, left-1, -1 ): #right 是1， left是0， 还得在多来一个
        #             #i = 1, 0 
        #             res.append(matrix[down][i])
        #         down -=1 #最下面一行结束了 = 1
            
        #     if left <= right :

        #         for i in range(  down , top-1   ,-1): # for i in range(1,0, -1),return 1 
        #             res.append(matrix[i][left])
        #         left +=1 

        
        # return res
    

        # left, right = 0 , len(matrix[0])-1 #用于列
        # #left = 0, right = 2
        # top , down = 0 , len(matrix) -1  #用于行
        # # top= 0 , down =2 



        # res = []


        # while left<= right and top <=down:

        #     #第一行， fix行不变，列变，并且top应该往下移动
        #     for i in range(left, right+1):
        #         res.append(matrix[top][i])
        #     top +=1 #top = 1了 , 第二轮top=2,加入了5

        #     for i in range(top,down+1): #第二轮空的 range(2,2),loop不run 
        #         res.append(matrix[i][right])
        #     right -=1 #right = 1 ， 第二轮right = 0 

        #     if top <= down: #第二轮2< =1 不成立，卡死，结束
        #         for i in range(right, left-1, -1 ): #return i = 1, 0 
        #             res.append(matrix[down][i])
        #         down -=1 #down =1 
        #     if left <= right : # 第二轮1<=0 不成立，卡死
        #         for i in range(down, top-1, -1 ):# return i = 1
        #             res.append(matrix[i][left])
        #         left +=1 #left =1
        # return res




        # #主要是matrix的index 的利用








        #practice 


        res = []


        top , down = 0, len(matrix) -1
        left, right = 0, len(matrix[0] )-1 #2

        while top <=down and left<=right: #< or <=?


            for i in range(left, right +1):
                res.append(matrix[top][i])

            top +=1

            for i in range(top, down+1):
                res.append(matrix[i][right ])
            right -=1

            if top <=down :
                for i in range(right, left-1,-1):
                    res.append(matrix[down][i])
                
                down -=1
            
            if left <= right:

                for i in range(down, top-1,-1):
                    res.append(matrix[i][left])
                left +=1

        return res












# @lc code=end

