#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode.cn/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (74.88%)
# Likes:    1576
# Dislikes: 0
# Total Accepted:    309.6K
# Total Submissions: 413.7K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
# 
# 
# 
# 
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # youtube neetcode讲解
        # # 获取数组的长度
        # n = len(nums) #4
        
        # # 使用前后缀乘积来解决这个问题
        # # 例如，对于数组 [1,2,3,4]，数字 2 对应的结果是 1*3*4。
        # # 其中，1 是前缀乘积，3*4 是后缀乘积。
        # # 因此，我们创建两个列表来存储前缀和后缀的乘积。
        # # 注意：为了方便计算，我们初始化这两个列表的所有元素为 1。(为了确保第0个元素前面有东西可以乘)
        
        # # 初始化前缀乘积数组
        # pre = [1] * n  ## pre = [1, 1, 1, 1]
        
        # # 初始化后缀乘积数组
        # suf = [1] * n # suf = [1, 1, 1, 1]
        
        # # 计算前缀乘积
        # for i in range(1, n): #由于我们第一个元素前面没有前缀，所以不动，直接pre的第一位是1，从第二个开始算
        #     # 当前元素的前缀乘积是前一个元素的前缀乘积乘以前一个元素的值
        #     pre[i] = pre[i-1] * nums[i-1] #
        #     #模拟：nums = [1,2,3,4]
        #     # 当 i = 1，对于2 来说，前缀: pre[1] = pre[0] * nums[0] = 1 * 1 = 1， pre = [1,1,1,1]
        #     # 这意味着 nums[0] 之前没有其他元素，所以前缀乘积是 1。
        #     # 当 i = 2对于3 来说，前缀: pre[2] = pre[1] * nums[1] = 1 * 2 = 2, pre = [1,1,2,1]
        #     # 这意味着 nums[1] 之前的所有元素的乘积是 1*2 = 2。
        #     # 当 i = 3: pre[3] = pre[2] * nums[2] = 2 * 3 = 6 , pre = [1,1,2,6]
        #     # 这意味着 nums[2] 之前的所有元素的乘积是 1*2*3 = 6。
        #     # [1, 1, 2, 6]

        # # 计算后缀乘积
        # for i in range(n-2, -1, -1): #倒着算，因为4后面没有后缀，所以suf的最后一个1 不动
        #     # n-2 = 2 , 到-1停止不包括-1，也就是到0 停止，
        #     # 反着从 2,1,0 位置取
        #     # 当前元素的后缀乘积是后一个元素的后缀乘积乘以后一个元素的值
        #     suf[i] = suf[i+1] * nums[i+1] # suf一开始是[1,1,1,1], 从倒数第二位开始改
        #     #模拟：nums = [1,2,3,4]
        #     # 当 i = 2: suf[2] = suf[3] * nums[3] = 1 * 4 = 4， suf = [1,1,4,1]
        #     # 这意味着 nums[2] 之后的所有元素的乘积是 4。
        #     # 当 i = 1: suf[1] = suf[2] * nums[2] = 4 * 3 = 12 , suf = [1,12,4,1]
        #     # 这意味着 nums[1] 之后的所有元素的乘积是 3*4 = 12。
        #     # 当 i = 0: suf[0] = suf[1] * nums[1] = 12 * 2 = 24 suf = [24,12,4,1]
        #     # 这意味着 nums[0] 之后的所有元素的乘积是 2*3*4 = 24。
        #     # 所以，suf 的值变为 [24, 12, 4, 1]。
    
        
        # # 初始化结果数组
        # ans = [1] * n
        
        # # 计算结果
        # for i in range(n):
        #     # 每个元素的结果是其前缀乘积乘以其后缀乘积
        #     ans[i] = pre[i] * suf[i]
        
        # # 返回结果数组
        # return ans

        n = len(nums)
        pre = [1]* n
        suf = [1]*n
        
        # nums = [1,2,3,4]
        # pre =  [1,1,2,6]
        # suf =  [24,12,4,1]
        for i in range(1,n):#nums第一个的前缀积没有，初始化为1，不用管，从第二位开始更新
            pre[i] = pre[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1): #最后一位的后缀积没有，初始化为1，从倒数第二位更新，index是2 ，1 ，0， 因此要反向取

            suf[i] = suf[i+1]*nums[i+1]

        result = [1]*n
        for i in range(n):# 0|1|2|3
            result[i] = pre[i]*suf[i]
        return result


        
        


       


# @lc code=end

