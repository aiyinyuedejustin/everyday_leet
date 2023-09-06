#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode.cn/problems/happy-number/description/
#
# algorithms
# Easy (63.43%)
# Likes:    1403
# Dislikes: 0
# Total Accepted:    415.3K
# Total Submissions: 654.5K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
# 
# 「快乐数」 定义为：
# 
# 
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 
# 
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# def x(a,b):
#     my_set = set() #set不能重复
#     while n!= 1: #先判断corner solution
#         n = sum(int(i) **2 for i in str(n)) #sum平方操作
#         #判断有无出现过，如果有，说明死循环了，不是快乐数字
#         if n in my_set:
#             return False
#         my_set.add(n)
#     return True
# 
# 示例 2：
# 
# 
# 输入：n = 2
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()# 先建立一个set，其实seen =[]也行

        while n != 1: #先判断目前是不是1

            n = sum(int(i) ** 2 for i in str(n)) # 如12， 就会是1**2 + 2**2
            if n in seen:  #这个sum曾经出现过，说明已经陷入了无限循环了，立刻return false
                return False
            seen.add(n) #否则往set里面加
        return True
# @lc code=end

