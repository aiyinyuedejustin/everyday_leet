#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode.cn/problems/integer-break/description/
#
# algorithms
# Medium (62.32%)
# Likes:    1255
# Dislikes: 0
# Total Accepted:    278.2K
# Total Submissions: 446.4K
# Testcase Example:  '2'
#
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 
# 返回 你可以获得的最大乘积 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 
# 
# 提示:
# 
# 
# 2 <= n <= 58
# 
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        

        # dp[i]：分拆数字i，可以得到的最大乘积为dp[i]。注意i是正整数，所以dp[1] =1 从1开始
        # j: 拆分后的第一个数字， 如j= 1,2,3,4....i， j>=1
        # 递推公式有2个：
        #  联想剪绳子：先切一段绳子长度为j，剩下的i-j可以选择切（dp[i-j]）或者不切(i-j)
        #  所以：
        #  j * (i - j) 是单纯的把整数拆分为两个数相乘，而j * dp[i - j]是拆分成两个以及两个以上的个数相乘。
        #  所以max(j * (i - j),j * dp[i - j] )是递推公式

        # 严格从dp[i]的定义来说，dp[0] dp[1] 就不应该初始化， 拆分0和拆分1没有意义，
        # 所以这里dp[0]= dp[1]  =0, 只初始化dp[2] = 1，然后从i=3开始循环""
        dp = [0] * (n+1) #dp[0]= dp[1]  =0 ，创建全是0的数组
        dp[2] = 1 #初始化dp2 =1
        if n == 2: #2 <= n <= 58
            return 1
        
        for i in range(3, n+1): #2 <= n <= 58
            for j in range(1, n//2+1): #j 要从1开始, 比如4拆成3+1, 1+3，其实重复到一半就够了
                #j 应该小于i，因为i最大取n， 如一个数字10，最多拆到9+1（j=9）， 再往后10+0就不对了,所以j最多到n-1
                dp[i]= max(max(j * (i - j),j * dp[i - j] ), dp[i])
                # '''
                # 首先fix i不变，看内部的j循环。
                # 创建数组的时候，dp[3]=0 at first， 当j = 1 时，
                # if max(j * (i - j),j * dp[i - j]）=5 ，就可以更新dp[3] =5，
                # 但我们就是想让dp[i]最大， 如果在j = 5时，max(j * (i - j),j * dp[i - j]）=2 了，
                # 那如果只用这一个max，那可能dp[i]被修改了，并不是j循环中真正的最大值，这样不行，
                # 所以要外面再套一层max，只有max(j * (i - j),j * dp[i - j]）比以往的dp[i]都大的时候才更新
                # 因此这里还要加一个单独的dp[i]用于保留record
                # '''
        return dp[n]




# @lc code=end

