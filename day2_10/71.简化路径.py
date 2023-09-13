#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#
# https://leetcode.cn/problems/simplify-path/description/
#
# algorithms
# Medium (44.28%)
# Likes:    643
# Dislikes: 0
# Total Accepted:    194K
# Total Submissions: 437.6K
# Testcase Example:  '"/home/"'
#
# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。
# 
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..）
# 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。
# 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。
# 
# 请注意，返回的 规范路径 必须遵循下述格式：
# 
# 
# 始终以斜杠 '/' 开头。
# 两个目录名之间必须只有一个斜杠 '/' 。
# 最后一个目录名（如果存在）不能 以 '/' 结尾。
# 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 
# 
# 返回简化后得到的 规范路径 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：path = "/home/"
# 输出："/home"
# 解释：注意，最后一个目录名后面没有斜杠。 
# 
# 示例 2：
# 
# 
# 输入：path = "/../"
# 输出："/"
# 解释：从根目录向上一级是不可行的，因为根目录是你可以到达的最高级。
# 
# 
# 示例 3：
# 
# 
# 输入：path = "/home//foo/"
# 输出："/home/foo"
# 解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
# 
# 
# 示例 4：
# 
# 
# 输入：path = "/a/./b/../../c/"
# 输出："/c"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# path 由英文字母，数字，'.'，'/' 或 '_' 组成。
# path 是一个有效的 Unix 风格绝对路径。
# 
# 
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # https://www.youtube.com/watch?v=aDQlRwbwlyI&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
       
       
        # unix path
        # .是目前folder
        # .. 回到上一个folder
        # // 或两个以上/， 可以当成/
        # 其他形式 如 ... “abcd"当成folder


        #input path 都从/ 开始
        # 两个以上的folder 中间被/分开
        #path 的尾巴没有/
        # 

        # 1. 用stack 放folder或者directory name
        # 2。 用split('/') 分开 
        # 3. 遍历分开后的list：
        #           3.1 如果是.. 那看stack是不是空，如果不是空就pop（因为..是想去上一个folder；比如/a/b/.. 目前在b，但其实是想回到a，那就直接pop掉b
#                     3.2 如果是.或者空，那就遍历下一个（没卵用
#                       3.3 不然的话， 就append 到stack里
        # 4. 把stack拿出来用/ 和.join method做 新路径， string

        stack = []

        for splited in path.split('/'):
            if splited == '..':
                if stack:
                    stack.pop()
            
            elif splited =='.' or splited =="":
                continue
            else:
                stack.append(splited)
        
        return '/'+'/'.join(stack)

#O(N) 
#O(2N) : stack+split 两个







# @lc code=end

