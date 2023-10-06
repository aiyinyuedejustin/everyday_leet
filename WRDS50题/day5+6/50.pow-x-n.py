#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.cn/problems/powx-n/description/
#
# algorithms
# Medium (37.98%)
# Likes:    1235
# Dislikes: 0
# Total Accepted:    396.7K
# Total Submissions: 1M
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，x^n^ ）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 
# 
# 示例 2：
# 
# 
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 
# 
# 示例 3：
# 
# 
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# 
# 提示：
# 
# 
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n 是一个整数
# 要么 x 不为零，要么 n > 0 。
# -10^4 <= x^n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. anything to pow of 0 
        #2. 如果n is odd:
        #x^5 ->x*x^4 ->x*x* x^3 ---->>>> 直到x^0停止
        #所以x^n = x* myPow(x,n-1) #递归，直到n=0 
        # 3. if n is even 
        # x^4 = x^2 * x^2 
        #所以 x^n ,存一个temp = pow(x, n/2)
        # 然后 temp自己又会自己一直整除2 下去
        #最终x^n  = temp *temp

        # 4. n<0 : if n = -3, x先变为1/x ,然后判断n的奇偶， 然后像上面一样继续
        if n ==0:
            return 1
    
        elif n <0 :
            #n is even
            return self.myPow(1/x, -n ) #然后他自己会进去判断奇偶

        #n is odd
        elif n %2 == 0 : #even
            temp = self.myPow(x, n/2)
            return temp *temp
        else:
            return x* self.myPow(x,n-1)
        
    


        

        # recurssion
# @lc code=end

