#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode.cn/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (64.13%)
# Likes:    2272
# Dislikes: 0
# Total Accepted:    342K
# Total Submissions: 533.3K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,3,4,2,2]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,1,3,4,2]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
# 
# 
# 
# 
# 进阶：
# 
# 
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode


        #不能修改，O（1） 的space complexity

        #两步骤
        # （1） linkedlist cycle
        # （2） floyd's 

        # Floyd's cycle detection-- 其实数字都是[1,n] 之间，想想成除了index0之外的，
        # 都point到其他点上，所以变成了一个linkedlist， 然后这list一定有个loop，
        # loop的entrance就是重复的那个数字\
        #  Except for index 0, each index in the array can be considered as a node in a linked list, 
        # where the value at that index is a pointer to another index.
        # Since there is a duplicate, there must be a cycle (loop) in this "linked list."

        # For example, if index 1 has the value 3, you can think of this as the node at index 1 "pointing" to index 3.

        # Step 1: Identify the point where the two pointers meet within the loop (cycle).
        # Step 2: Find the entry point of the loop, which is the duplicate number.
        
        
        # For the example nums = [1, 3, 4, 2, 2]:
        # - Index 0 has value 1, so it points to index 1.
        # - Index 1 has value 3, so it points to index 3.
        # - Index 3 has value 2, so it points to index 2.
        # - Index 2 has value 4, so it points to index 4.
        # - Index 4 has value 2, so it points back to index 2.

        # The pointing sequence would look like this:
        # 0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 -> ...
        # Notice that there is a cycle formed by index 2 and index 4.
        #1 找到两个点相交

        slow, fast = 0,0 

        while True:
            slow = nums[slow] #slow = slow.next
            fast = nums[nums[fast]] #类似于fast.next.next 

            if slow == fast:
                break
        #第二轮           
        slow2 = 0 
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2 #直接找到入口



# On
# O1



# @lc code=end

