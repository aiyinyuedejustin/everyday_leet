#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode.cn/problems/4sum/description/
#
# algorithms
# Medium (36.81%)
# Likes:    1745
# Dislikes: 0
# Total Accepted:    503.2K
# Total Submissions: 1.4M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
# 
# 
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# 你可以按 任意顺序 返回答案 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:

    from collections import defaultdict
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #与三数之和类似，双指针（先看15题
        # 15.三数之和 (opens new window)的双指针解法是一层for循环num[i]为确定值，然后循环内有left和right下标作为双指针，找到nums[i] + nums[left] + nums[right] == 0。
        # 四数之和的双指针解法是’两层‘for循环，nums[k] + nums[i]为确定值，依然是循环内有left和right下标作为双指针，找出nums[k] + nums[i] + nums[left] + nums[right] == target的情况，三数之和的时间复杂度是O(n^2)，四数之和的时间复杂度是O(n^3) 。
        #注意跟三数之和不同的是，4个数加起来是target，而不是3个数相加为0，注意剪枝和去重 
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n): #第一层循环
            #1. 坑，此处target可能为负。如果采用3数之和sort后第一个数字必然<=0，那就错了。
            # \e.g.[-4, -3, -2, -1]，target是-10，不能因为-4 > -10而直接return result。而是应该加些条件
            if nums[i] > target and nums[i] > 0 and target > 0:# 剪枝（可省）【必须限制都是正数的情况下，排序后，num[i]>target才可以跳过当前i
                break#可以写break或者return result，因为这是最外层循环，最外层停止就全停，直接跳到最后return result
            if i > 0 and nums[i] == nums[i-1]:# 去重i,类似三数之和 ，从1开始
                continue
            for j in range(i+1, n):#第二层循环， j初始为i+1
                if nums[i] + nums[j] > target and nums[i] + nums[j] > 0 and target > 0: #剪枝（可省） #此时相当于，sort后，在正数的情况下nums[i] + nums[j]作为一个整体，可以break掉
                    break #一定要写break，因为外面还有一层循环可以继续，不然这里return result全停下来，会错失一些其他i的结果
                
                
                if j > i+1 and nums[j] == nums[j-1]: # 去重j。j是从i+1开始的所以要向后一个。类似上面的i，是从0开始的，但要从1开始
                    continue
                left, right = j+1, n-1  
                while left < right: #跟三数之和一样
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        #去重left right
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result

        



# @lc code=end

