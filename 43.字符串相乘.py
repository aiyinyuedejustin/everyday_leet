#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode.cn/problems/multiply-strings/description/
#
# algorithms
# Medium (44.37%)
# Likes:    1256
# Dislikes: 0
# Total Accepted:    310.8K
# Total Submissions: 700.4K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
# @lc code=end

