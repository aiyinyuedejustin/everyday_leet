#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#
# https://leetcode.cn/problems/integer-to-english-words/description/
#
# algorithms
# Hard (36.49%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    38.6K
# Total Submissions: 105.9K
# Testcase Example:  '123'
#
# 将非负整数 num 转换为其对应的英文表示。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 123
# 输出："One Hundred Twenty Three"
# 
# 
# 示例 2：
# 
# 
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"
# 
# 
# 示例 3：
# 
# 
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
# @lc code=end

