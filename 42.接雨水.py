#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (63.09%)
# Likes:    4709
# Dislikes: 0
# Total Accepted:    768.3K
# Total Submissions: 1.2M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 
# 
# 示例 2：
# 
# 
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        #https://www.youtube.com/watch?v=PTZIPx9pzTY&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        
        #初始化全局最高点的index 为0 
        # 初始化water =0
        # 初始化左右两侧 的最高的高度=0 
        #1. for loop 找全局最高点 


        #  2.  定义左右两个指针，初始化为0 ，记录左右两侧的最高点的高度
        # 能接住的雨水就是左右两侧最高点-当前位置
        #3， 从左往右， 从右往左各一个for loop
        # 持续2 的动作，总水量最后sum 左右两侧即可

        # water = 0 #总水量
        # peak_idx = 0 #全局最高点idx
        # left_height = 0
        # right_height = 0

        # #找全局最高点
        # for i in range(len(height)):
        #     if height[i] >height[peak_idx]: #不能用max，不然只知道max 而不知道index
        #         peak_idx = i 

        # # 左边水量
        # for i in range(peak_idx+1): #直到全局最高点(包含)
        #     if height[i] > left_height: #当前位置高度 比之前的左侧的高度大
        #         left_height = height[i] #更新左侧最高点的高度
        #     else: #一定是else，因为左侧最高点更新后，不会跟自己相减，
        #         # 一定是这轮更新后，下一轮跟他右侧比较高度。如第一次左侧最高点更新为1， 下一轮当前位置高度0 ，这时候才有1-0=0
        #         water = water + (left_height - height[i]) # 左侧最高点减去当前位置高度就是新增的水
                       

        # for i in range(len(height)-1,peak_idx-1,-1): #由于算左侧水量的时候，peak_idx已经包含，这里就不用再算一次
        #     if height[i] > right_height:
        #         right_height = height[i]
        #     else:
        #         water = water + right_height-height[i]
        # return water


        peak = 0 #index
        water = 0
        left_most=0 #高度
        right_most = 0

        for i in range(len(height)):
            if height[i]>height[peak]:
                peak = i

        for i in range(peak+1):
            if height[i] > left_most:
                left_most = height[i]
            else:
                water = water + left_most - height[i]
        
        for i in range(len(height)-1,peak,-1):
            if height[i] > right_most:
                right_most = height[i]
            else:
                water = water + right_most - height[i]
        return water
        
        




        


# @lc code=end

