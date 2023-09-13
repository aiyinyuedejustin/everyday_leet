#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode.cn/problems/merge-sorted-array/description/
#
# algorithms
# Easy (52.82%)
# Likes:    2126
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m
# 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并 [1] 和 [] 。
# 合并结果是 [1] 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是 [] 和 [1] 。
# 合并结果是 [1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
# 
# 
# 
# 
# 提示：
# 
# 
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[j] <= 10^9
# 
# 
# 
# 
# 进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # https://www.youtube.com/watch?v=P1Ic85RarKY&ab_channel=NeetCode
        # 对[1,2,3,0,0,0]， 倒着填，对于最后一位，左指针指向最后一个实数3， 
        # 对[2,5,6] ，右指针指向 6， 
        # 对比3和6， 如果6大，就填进去，右指针移动左
        # 下一次对比3和5， 同样填，右指针移动左
        # 最后对比3和2， 此时应该调换顺序


        # m n last 都是index，也可以当做指针

        # 1. last index in nums1
        last = m+n -1 #用于填数字的指针,初始于nums1的0的最后一位
        #2. merge in reverse order
        while m>0 and n>0 : #index必须合法，m是nums1 本身数字  的length
            if nums1[m-1] >nums2[n-1]: 
                nums1[last] = nums1[m-1] #按升序排，所以谁大就填谁
                m -=1 #左指针移动,谁大就动那个指针往前移动
            else:
                nums1[last] = nums2[n-1]
                n -=1 #右指针移动，,谁大就动那个指针往前移动，因为用掉了他这个数字
            last -=1 #填数指针移动， 不管怎样已经填了

        # 3. fill nums1 with leftover in nums 2 
        while n>0:
            # cornor case1: 
            # nums1 = [4,5,6,0,0,0]
            # m = 3
            # nums2 = [1,2,3]
            # n = 3, 初始化fast=5
            #上一个while运行完事时，由于所有nums1都比nums2大，nums1实际变成[4,5,6,4,5,6]， 但nums2还没用呢

            # cornor case 2: 
            # nums1 = [0]
            # m = 0
            # nums2 = [1]
            # n = 1, 初始化fast= 0+1-1= 0,由于m已经为0，我们不会进入第一个while循环。但我们最终答案应该是[1]因此要用第二个循环处理
            nums1[last] =nums2[n-1]
            n, last = n-1, last-1 #同时更新即可


# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

# #初始化3个指针，一个指向填数，一个指向m-1（nums1最后),一个指向n-1(nums2最后)
#         last = m+n-1

#         while m>0 and n>0 :
#             if nums1[m-1] < nums2[n-1]:
#                 nums1[last] = nums2[n-1] #谁大填谁
#                 n-=1 #用完了就往前移
#             else:
#                 nums1[last] = nums1[m-1]
#                 m-=1
#             last-=1

#         while n>0:
#             nums1[last] = nums2[n-1]
#             last-=1
#             n-=1




# @lc code=end

