#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode.cn/problems/two-sum/description/
#
# algorithms
# Easy (52.96%)
# Likes:    17597
# Dislikes: 0
# Total Accepted:    4.8M
# Total Submissions: 9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 
# 你可以按任意顺序返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 只会存在一个有效答案
# 
# 
# 
# 
# 进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        # 可以用字典法 或者集合
        # 集合：
        # 输入：nums = [2,7,11,15], target = 9
        # 输出：[0,1]

        #创建一个set
        my_set = set() #存放遍历过的元素
        #遍历nums的每一个，同时返回index
        for index, num in enumerate(nums):

        #计算compliment
            compliment = target - num 

            if compliment in my_set:
                return [index,nums.index(compliment)]
            else:
                my_set.add(num)

        # 如果compliment在set里面，说明当前数字和其compliment互补刚好凑target
        # 所以返回当前数字的index和 nums里面compliment 的index
        # 如果不是应该加入当前数字而不是compliment，因为每次for 是针对当前数字的，
        # 如上面例子，对于2 ，compliment是7， 如果把7加入myset，永远也找不到
        # 反之，加入2， 第二次对于7时compliment是2，刚好找到

# @lc code=end

