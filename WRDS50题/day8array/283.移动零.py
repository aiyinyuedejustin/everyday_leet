#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode.cn/problems/move-zeroes/description/
#
# algorithms
# Easy (63.60%)
# Likes:    2208
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [0]
# 输出: [0]
# 
# 
# 
# 提示:
# 
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# 
# 进阶：你能尽量减少完成的操作次数吗？
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """



        left = 0

        for right in range(len(nums)):
            if nums[right] !=0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1 

        # 不能用 extra memory， 必须inplace
        #  quick select

        # 或者说，把所有non zero 移动到左边，这个题目描述很迷惑

        # # l 一直保持最左侧指向某个0， right 一直移动，然后互换，这样可以保证一直指向想交换的位置


        # l = 0 

        # for r in range(len(nums)): #right 要一直移动，什么时候交换了就换l+1

        #     if nums[r] != 0 :
        #         nums[r], nums[l] = nums[l], nums[r] #swap
        #         l +=1
            


# @lc code=end

