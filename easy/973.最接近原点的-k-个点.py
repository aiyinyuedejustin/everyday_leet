#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
# https://leetcode.cn/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (65.27%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    96.8K
# Total Submissions: 148.3K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0)
# 最近的 k 个点。
# 
# 这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)^2 + (y1 - y2)^2 ）。
# 
# 你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：points = [[1,3],[-2,2]], k = 1
# 输出：[[-2,2]]
# 解释： 
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[3,3],[5,-1],[-2,4]], k = 2
# 输出：[[3,3],[-2,4]]
# （答案 [[-2,4],[3,3]] 也会被接受。）
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
# 
# 
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #不需要开根号，反正只看绝对距离也行
        points.sort(key = lambda  x: x[0]**2 +x[1]**2)
        return points[:k]



# 11111111111111111
        # 可以用堆排序，快速排序
        #目前这里用偷懒法

        # # 创建一个空列表来存储每个点的索引和它到原点的距离
        # distance = []
        # # 创建一个空列表来存储结果
        # res = []

        # # 遍历每个点
        # for i in range(len(points)):
        #     point = points[i]
        #     # 计算点到原点的距离的平方（不需要开方，因为我们只是比较大小，不需要确切的距离值）
        #     dis = point[0]**2 + point[1]**2
        #     # 将点的索引和距离添加到distance列表中
        #     distance.append([i, dis])

        # # 根据距离对distance列表进行排序，进去之后使用每个小列表的第二个。
        # #data.sort(key=lambda x: x[1], reverse=True)是反过来
        # distance.sort(key=lambda x:x[1])

        # # 获取前k个距离最小的点
        # for i in range(k):
        #     #distance[i][0] 是获取index
        #     res.append(points[distance[i][0]])
        # return res
# 2222222222222222
        # idx_distance = []
        # result_list = []

        # # points = [[1,3],[-2,2]], len points = 2 
        # for i in range(len(points)):
        #     each_point = points[i]
        #     distance = each_point[0]**2 + each_point[1]**2 #不用开平方

        #     idx_distance.append([i,distance])
        
        # idx_distance.sort(key= lambda x : x[1]) #按照第二个排序, 目前原始index被打乱，需要从poitns中提取原数据点
        # #[[1,8],[0,10]],  
        # for i in range(k): 
        #     result_list.append(points[idx_distance[i][0]])

        # return result_list
    
### 3333333
        # points.sort(key = lambda x: x[0]**2 + x[1]**2) #sort不会return任何东西
        # return points[:k]
        #sorted可以return东西
        # x = sorted(points, key = lambda x : x[0]**2 +x[1]**2)
        # return x[:k]













# @lc code=end

