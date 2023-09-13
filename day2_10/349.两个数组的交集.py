#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode.cn/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (74.19%)
# Likes:    819
# Dislikes: 0
# Total Accepted:    476.8K
# Total Submissions: 642.8K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #双指针
        i, j = 0,0
        output = []
        nums1, nums2 = sorted(nums1), sorted(nums2)

        while i < len(nums1) and j<len(nums2):# 从左往右，不能超边界
            if nums1[i]< nums2[j]: #因为sort了，i的数小就把i增加，让他靠近j的数字
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                output.append(nums1[i])
                i+=1 
                j+=1 #要同时移动了
        
        output = list(set(output))#防止出现不唯一的情况，如nums1 = [222] nums2 = [222]
        return output



# @lc code=end

