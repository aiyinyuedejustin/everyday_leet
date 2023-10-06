#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode.cn/problems/next-permutation/description/
#
# algorithms
# Medium (38.51%)
# Likes:    2316
# Dislikes: 0
# Total Accepted:    456.3K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
# 
# 
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 
# 
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列
# 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
# 
# 
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 
# 
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
# 
# 必须 原地 修改，只允许使用额外常数空间。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://www.youtube.com/watch?v=JRgIqugFhTo&ab_channel=CrackingFAANG
        #很抽象，但是步骤：
        #1. 找到pivot，就是左半部分停止升序的最后一个
        #2. 把pivot 和右侧所有数中，比pivot大的里面最小的那个swap， 如145 | 87，145是升序sort的，87是降序sort的。5是升序sort的最后一位
        # pivot就是5，  右侧比5大的第一个是7，把5和7调换位置，此时变成 147|85， 
        # 3。然后把后半部分反转，就得到了14758，就是next permutation
        #注意所有已有的合理排列，要么都是升序，要么一半升序一半降序，要么全降序，
        pivot = None #初始没有pivot所以null

        for  i in range(len(nums) -1 , 0, -1): #从右往左，取不到index 0 。因为我们对比i和i-1，i 最小是1，取不到0
            if nums[i] >nums[i-1]: #145 87,前半部分肯定是sort的，后半部分不是。index从大到小。
                # nums[3]=8 > nums[2]=3. 那么pivot 的index是2
                pivot = i-1 #index of pivot
                break # break this loop 
            
        else: #else for loop:如果loop 完全执行完了没有break才会执行这个。这说明nums本身就是完全降序的如【54321】
            nums.reverse() #那此时reverse 即可
            return #停，不然继续运行下面不对了
        
        #  find the smallest number to the right of pivot  and it's larger than pivot
        swap = len(nums) -1 #依然从右往左
        while nums[swap] <= nums[pivot]: # 必须写<= #因为我们要找至少比pivot大的数去swap，如124 82, pivot 在4，我们应该跟8换而不是2，所以要加while
            #开始找最小的，比pivot大的数。但对于145 87 这个例子，nums[4]=7 > nums[pivot]=5, 所以这个不执行，刚好最后一个就是最大的
            # 注意如果是一半升一半降，第二部分一定都是降序，只不过可能是124 82, pivot 在4，我们应该跟8换而不是2，所以要加while
            swap -= 1
        
        nums[pivot], nums[swap] = nums[swap], nums[pivot]# 互换两数

        nums[pivot +1 :] = reversed(nums[pivot +1 :]) #把pivot右半部分 reverse， reversed会返回。而.reverser不会返回

        return #这个return其实可以不要

#O (N) + O(N) = O(N)
# O(1)

# @lc code=end

