#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
# https://leetcode.cn/problems/reorganize-string/description/
#
# algorithms
# Medium (48.54%)
# Likes:    490
# Dislikes: 0
# Total Accepted:    53.3K
# Total Submissions: 109.8K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。
# 
# 返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "aab"
# 输出: "aba"
# 
# 
# 示例 2:
# 
# 
# 输入: s = "aaab"
# 输出: ""
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length <= 500
# s 只包含小写字母
# 
# 
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
# @lc code=end

