#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode.cn/problems/ransom-note/description/
#
# algorithms
# Easy (61.04%)
# Likes:    782
# Dislikes: 0
# Total Accepted:    368.5K
# Total Submissions: 603K
# Testcase Example:  '"a"\n"b"'
#
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 
# 如果可以，返回 true ；否则返回 false 。
# 
# magazine 中的每个字符只能在 ransomNote 中使用一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote 和 magazine 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       #版本1、
        # 第一点“为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思”  这里说明杂志里面的字母不可重复使用。

        # 第二点 “你可以假设两个字符串均只含有小写字母。” 说明只有小写字母，这一点很重要

        #只需要考虑ransomNote有没有在magazine出现，而不需要考虑反过来
        #也就是说，ransomNote里面每个都要在magezine里面出现，且每个字母只能用一次。
        # 那么ransomeNote里面每个字母的数量一定要<= magzine里面每个字母的数量
        #先set一下确保不会重复遍历，
        #str.count() 方法在没有找到指定子字符串的情况下会返回 0。
        # 所以这个不等式既可以让ransomNote的字母在magazine出现，也确保每个字母只用一次
        return   all( ransomNote.count(c)  <= magazine.count(c) for c in set(ransomNote))
# @lc code=end

