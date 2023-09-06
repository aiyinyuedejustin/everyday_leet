#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode.cn/problems/4sum-ii/description/
#
# algorithms
# Medium (64.22%)
# Likes:    883
# Dislikes: 0
# Total Accepted:    221.4K
# Total Submissions: 344.8K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l)
# 能满足：
# 
# 
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
# 
# 
#

# @lc code=start
class Solution:
    from collections import defaultdict
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 先遍历AB两个，使用defaultdict设置默认值

        my_dict = defaultdict(int) #不能填0，必须要填一个函数进去。或者填lambda: 0
        cnt =0

        for i in nums1:
            for j in nums2:
                my_dict[i+j] += 1 #让每个和作为key，次数作为value
        
        for i in nums3:
            for j in nums4:
                # my_dict.get(-(i+j), 0) 会尝试查找键 -(i+j) 在字典 rec 中对应的值也就是上面i+j的次数
                # 如果找到了，就返回该值；如果没有找到，就返回 0。
                 # a+b=−(c+d)⟹a+b+c+d=0， 所以a+b其实匹配-(c+d)就代表这四个数sum=0
                cnt += my_dict.get(-(i+j),0) # 如AB两个list里面和为0的出现了2次，这里-(c+d)出现一次，那么2x1 =2， 说明一共匹配2次，cnt+2

        return cnt

        # nums1 = [1, 2]
        # nums2 = [-1, -2]
        # nums3 = [1, 2]
        # nums4 = [-1, -2]

        # 步骤 2：计算 nums1 和 nums2 的所有可能的两数之和，并记录在 rec 中。

        # 当 i = 1, j = -1，i+j = 0，rec[0] = 1
        # 当 i = 1, j = -2，i+j = -1，rec[-1] = 1
        # 当 i = 2, j = -1，i+j = 1，rec[1] = 1
        # 当 i = 2, j = -2，i+j = 0，rec[0] = 2（因为 0 已经出现过一次）
        # 现在，rec = {0: 2, -1: 1, 1: 1}

        # 步骤 3：遍历 nums3 和 nums4 的所有元素组合，查找它们的和的负数在 rec 中出现的次数。

        # 当 i = 1, j = -1，-(i+j) = 0，cnt += rec.get(0, 0) = 2 # -(c+d)= 0 匹配上面和为0的是2次，cnt+2
        # 当 i = 1, j = -2，-(i+j) = 1，cnt += rec.get(1, 0) = 1
        # 当 i = 2, j = -1，-(i+j) = -1，cnt += rec.get(-1, 0) = 1
        # 当 i = 2, j = -2，-(i+j) = 0，cnt += rec.get(0, 0) = 2
        # 最终，cnt = 2 + 1 + 1 + 2 = 6

        # 步骤 4：返回 cnt，即 6，这就是满足条件的 (i, j, k, l) 组合的数量。

       
# @lc code=end

