#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode.cn/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.32%)
# Likes:    2572
# Dislikes: 0
# Total Accepted:    504.7K
# Total Submissions: 1M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回 滑动窗口中的最大值 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], k = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 用q+sliding window

#         双端队列法（推荐）：

# 使用一个双端队列存储数组的索引，注意是存index，确保队列的头部始终是当前窗口的最大值。(如果新的值比当前大，那就得全部弹出)
# 当新元素进入窗口时，从队列尾部开始比较，如果新元素大于或等于尾部元素，则将尾部元素弹出，直到新元素小于尾部元素或队列为空。
# 将新元素索引加入队列。
# 检查队列头部的索引是否仍在窗口内（即是否超出窗口的左边界），如果超出，则从头部弹出。
# 每次滑动时，队列的头部元素就是当前窗口的最大值。
# 这种双端队列法的时间复杂度为O(n)，因为每个元素最多进入和退出队列一次。

# value in q is always in decresing order [5,3,1]
#compare the value and the right most value in q, if value > q, which means need to popright,
# remove rihgt moust element from q if current value is greater, 
#eg . q = [5,3,1], if value =2, remove 1 
# and append left most value from q to result(which is the max value)

#if out of bound for window, popleft the leftmost value 



#注意q用来存的是index
        #cornor
        if k ==1:
            return nums

        q = deque()

        res = []
        

        start = 0  #index 

        for end in range(len(nums)): #move right index

            #先检查q里right most 是不是小于current，如果是我们要pop了. 虽然存的是index，但要保证q代表的nums里面的值是decreaing order， 这样最左边永远最大
            while q and nums[q[-1]] < nums[end]:
                q.pop()
            q.append(end)
# This line ensures that the deque q maintains its elements in a decreasing order. 
# It keeps popping the elements from the right until the rightmost element in the deque is greater 
# than the current element (nums[end]).
         
            if q and q[0] == end-k: #如果当前队列最左侧存储的下标等于 i-k 的值，代表目前队列已满。
                q.popleft() #remove that left most 
# This line checks if the leftmost index in the deque is end - k. If it is, 
# that means that this index is now out of the current window of size k, 
# and therefore needs to be removed. This ensures that only elements in the 
# current window are considered.


            if end-start +1 == k: #只有当size是k的时候才会加入 res
                res.append(nums[q[0]]) #是leftmost指针指向的是最大
                start +=1
                # This checks if the current window size is k. If it is, then we append the
                # maximum element of the current window to the result.
                # This is guaranteed to be the leftmost element in q
        return res




# On

# On -- n is size of output
# @lc code=end

