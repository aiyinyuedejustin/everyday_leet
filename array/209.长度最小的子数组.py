 #
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (46.59%)
# Likes:    1855
# Dislikes: 0
# Total Accepted:    599.4K
# Total Submissions: 1.3M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
# 
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #用滑动窗口思想，right是窗口末尾位置。其实也是类似双指针
        left = 0  #index
        right = 0  #index
        cum_sum = 0 #初始化滑动窗口累加
        min_length = len(nums)+1000 #为了满足后面min的其中一个值，弄个很大的
        
        while right < len(nums):# 滑动窗口上限
            cum_sum = cum_sum + nums[right] 

            while cum_sum >= target: #不能用if，不然左侧不能持续移动，此处为了移动左侧
                min_length = min(min_length, right-left +1)# 看当前符合条件区间的长度,作为最小长度
                cum_sum = cum_sum-nums[left]#减去左侧的值，并且下一步移动左侧，继续while看还符不符合条件。如外层while右侧+5，左侧好几个1，可以依次减掉，找到最短长度
                left = left +1 # 移动左侧，如果ok的话，一直重复上面操作直到cum_sum 小于target，然后继续移动右侧


            right += 1 #移动右侧
        return min_length if min_length != len(nums)+1000 else 0 #如果整个全加起来都不符合，minlenght就应该返回0
# @lc code=end

