#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (63.21%)
# Likes:    2285
# Dislikes: 0
# Total Accepted:    921.5K
# Total Submissions: 1.5M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
# 
# 
# 
# 提示： 
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # https://www.youtube.com/watch?v=ryF_f9tZIqw&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        # min heep , 每次加入一个自动排序，
        #当数量比k多，就pop掉第一个，也就是最小的那个，保持heap里面都至少比以前大or相等
        # 最后，return heap[0]

        min_heap = []
        for num in nums:
            if len(min_heap) <k: #没有达到k的时候无脑加
                heapq.heappush(min_heap,num)

            else: #当达到k个后，想要维持k个，只能加一个减一个
                heapq.heappushpop(min_heap,num) #先加入，再弹出，相当于维持目前k个。
                # 如果真的比当前所有元素大，加入后pop顶端小的。
                #如果比当前元素小，加入后在弹出，哪也不变

        return min_heap[0]


# O（nlog k
# @lc code=end

