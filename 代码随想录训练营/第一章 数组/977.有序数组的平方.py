#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode.cn/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (67.89%)
# Likes:    878
# Dislikes: 0
# Total Accepted:    572.5K
# Total Submissions: 843.4K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
# 
# 示例 2：
# 
# 
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 10^4
# -10^4 
# nums 已按 非递减顺序 排序
# 
# 
# 
# 
# 进阶：
# 
# 
# 请你设计时间复杂度为 O(n) 的算法解决本问题
# 
# 
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # #因为有序，且有负数，所以平方后最大数字在两侧。可以用双指针。
        # #思路： 比较最左侧和最右侧的平方，如果是最右侧的平方大，那么就把新数组最右边的（最大值）赋予最右侧数字的平方，
        # # 并且把原数组右侧index向左移动。 反之，移动最左侧的index+1。并且每次新数组更新位置的index向左移动
        # left = 0  #index
        # right = len(nums)-1 # index

        # update_index = len(nums) -1 #从最右侧（最大值）开始更新，依次向左

        # result = [0] * len(nums) #初始化同样大小的数组

        # while left <= right: # 两者可以相等，就是最后一个元素
        #     if nums[left] ** 2 < nums[right] ** 2: #前面说了，有序的，且最大值一定出现在两侧。这里直接从两侧向中间靠拢
        #         result[update_index] = nums[right] ** 2 # result的最大值（也就是最右侧，因为要非递减顺序
        #         right = right -1 #右侧指针向左移动一个
        #     else: #如果是左侧大
        #         result[update_index] = nums[left] ** 2
        #         left = left +1
        #     update_index -= 1 # 当前最大值的index向左，
        
        # return result


        l , r = 0 , len(nums)-1
        update_index = len(nums) -1
        res = [0]* len(nums)
        while l <= r: 
            if nums[l]**2 < nums[r]**2:
                res[update_index] = nums[r]**2
                r -=1
            else:
                res[update_index] = nums[l]**2
                l+=1
            update_index -=1
        return res
            


                
 
# @lc code=end

