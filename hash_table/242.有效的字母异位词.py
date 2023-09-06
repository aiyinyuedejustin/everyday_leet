#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (65.92%)
# Likes:    839
# Dislikes: 0
# Total Accepted:    647.5K
# Total Submissions: 982.2K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 



    
        
# 示例 2:
# 
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 
# s 和 t 仅包含小写字母
# 
# 
# 
# 
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #ord()会返回ascll码，那么ord(a)和ord（b）就会差1.
        #利用这ord(b)-ord(a)我们
        #初始化空数组
        array = [0]*26 # 字母一共有26个
        #遍历s，对于所有字母我们在空数组index上都+1
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了,把ord（a)当做index 0 即可
            array[ord(i)-ord('a')] +=1 

        #遍历t，对于所有字母我们在空数组index上都-1
        for i in t:
            array[ord(i)-ord('a')] -=1

        #如果最后数组的每一位有不是0的，说明s或者t的某个字母出现多了，return false
        for i in array:
            if i != 0:
                return False
        #如果都是0，那就合格
        return True
# @lc code=end

