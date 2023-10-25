#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode.cn/problems/single-number/description/
#
# algorithms
# Easy (72.89%)
# Likes:    3040
# Dislikes: 0
# Total Accepted:    985.7K
# Total Submissions: 1.4M
# Testcase Example:  '[2,2,1]'
#
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
# 
# 
# 
# 
# 
# 示例 1 ：
# 
# 
# 输入：nums = [2,2,1]
# 输出：1
# 
# 
# 示例 2 ：
# 
# 
# 输入：nums = [4,1,2,1,2]
# 输出：4
# 
# 
# 示例 3 ：
# 
# 
# 输入：nums = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# 除了某个元素只出现一次以外，其余每个元素均出现两次。
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #必须constant time +memory

        #这里可以用XOR， 0^a = a, a^a = 0, a^b^a = b
        #这里的a^b^a = b, 因为a^a = 0, 0^b = b

        #这里的思路是，如果一个数出现两次，那么就会被抵消，最后剩下的就是只出现一次的数
        a= 0 

        for i in nums:
            a ^= i
        return a

    


        # a = 0

        # for i in nums:
        #     a = a^ i
        # return a 






# @lc code=end

