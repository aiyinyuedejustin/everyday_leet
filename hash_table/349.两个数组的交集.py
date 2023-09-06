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
        #注意题目特意说明：输出结果中的每个元素一定是唯一的，也就是说输出的结果的去重的， 同时可以不考虑输出结果的顺序
        # 因此使用unordered set,其实python就是用set即可
        return list(set(nums1) & set(nums2))
    # return list(set(nums1).intersection(set(nums2)))也行
        # return list(set(nums1 & nums2)) #注意nums 是列表，要先转化为set才有&操作


# @lc code=end

