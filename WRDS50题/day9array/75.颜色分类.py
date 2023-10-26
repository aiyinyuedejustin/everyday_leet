#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode.cn/problems/sort-colors/description/
#
# algorithms
# Medium (60.68%)
# Likes:    1681
# Dislikes: 0
# Total Accepted:    575.2K
# Total Submissions: 948K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 
# 
# 
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 要排序但是不能用sort，one-pass +O(1)的sc


        # i 如果是0， 就跟左指针换， 并且i+1, left+1
        # 如果i是2 就跟右指针换、 right -1

        # 如果i是1，、自己+1

        left = 0
        right = len(nums)-1
        i = 0 


        while i <= right:
            if nums[i] ==0: #如果i和left在同一位置，就自己跟自己换，不变，但是会+1（遇到相同的情况
                nums[i], nums[left] = nums[left], nums[i]

                i+=1
                left +=1

            elif nums[i] ==2:
                nums[i], nums[right] = nums[right], nums[i]
                right -=1 
            else:
                i +=1 


# TC ON

#用constant space O1
# @lc code=end

