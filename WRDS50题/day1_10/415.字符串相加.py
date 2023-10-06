#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode.cn/problems/add-strings/description/
#
# algorithms
# Easy (54.75%)
# Likes:    789
# Dislikes: 0
# Total Accepted:    299.8K
# Total Submissions: 547.8K
# Testcase Example:  '"11"\n"123"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 
# 
# 示例 2：
# 
# 
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 
# 
# 示例 3：
# 
# 
# 输入：num1 = "0", num2 = "0"
# 输出："0"
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # https://www.youtube.com/watch?v=q1RR8gk47Cg&ab_channel=CrackingFAANG
        # #     457  -》 carry是1 ， 13进1，  13 进1. 最后一位下面的数字如果对不齐，补0
        # # +   077
        # # ----------
        # i = len(num1)-1 #最后一位，从后往前
        # j = len(num2) -1

        # carry = 0
        # res = []

        # while i >= 0 or j >=0:
        #     cur_i = int(num1[i]) if i>= 0 else 0 # 如77 ，指针向左移动，超过了第一位，就补0 ，因此else 0 
        #     cur_j = int(num2[j]) if j>= 0 else 0 

        #     cursum = carry + cur_i + cur_j

        #     res.append(str(cursum % 10)) # 5%3 = 2取余

        #     carry = cursum // 10 #取 进了几个1

        #     i -= 1 #向前移动处理下一位
        #     j -= 1

        # if carry: #最后carry还剩一位没进
        #     res.append(str(carry))
        
        # return "".join(reversed(res)) # 指针是从后往前动，但是res是从前往后加的，因此要反过来

        #双指针，i 和j代表两个str最后一位，依次向前移动




# 好的，我们将使用 num1 = "456" 和 num2 = "77" 来模拟这段代码，并详细跟踪所有变量的变化。

# 模拟:

# 初始化：

# i = 2 (指向 "456" 的最后一个字符 "6")
# j = 1 (指向 "77" 的最后一个字符 "7")
# carry = 0
# res = []
# 进入 while 循环，因为 i >= 0 和 j >= 0 都为真：

# cur_i = 6 (从 "456" 中取)
# cur_j = 7 (从 "77" 中取)
# cursum = 6 + 7 + 0 = 13
# res = ["3"] (从 cursum % 10 得到)
# carry = 1 (从 cursum // 10 得到)
# i 减少到 1，j 减少到 0
# 再次进入 while 循环，因为 i >= 0 和 j >= 0 都为真：

# cur_i = 5 (从 "456" 中取)
# cur_j = 7 (从 "77" 中取)
# cursum = 5 + 7 + 1 = 13
# res = ["3", "3"] (从 cursum % 10 得到)
# carry = 1 (从 cursum // 10 得到)
# i 减少到 0，j 减少到 -1
# 再次进入 while 循环，因为 i >= 0 为真，但 j >= 0 为假：

# cur_i = 4 (从 "456" 中取)
# cur_j = 0 (因为 j 已经超出 "77" 的范围)
# cursum = 4 + 0 + 1 = 5
# res = ["3", "3", "5"] (从 cursum % 10 得到)
# carry = 0 (从 cursum // 10 得到)
# i 减少到 -1
# 退出 while 循环，因为 i >= 0 和 j >= 0 都为假。

# 检查 carry，它现在是 0，所以不需要添加任何东西到 res。
# 使用 join 和 reversed 函数将 res 转换为字符串 "533"。

# 最终结果是 "533"。


        i = len(num1) -1
        j = len(num2) -1

        carry =0 

        res = []

        while i >=0 or j >=0:


            curi = int(num1[i]) if i>=0 else 0 
            curj = int(num2[j]) if j >=0 else 0 #"456", num2 = "77"， 77移动到0，前面要补0 

            cursum = carry + curi +curj

            res.append(str(cursum % 10)) #给res从后往前加入余数，但由于append是正向的，最后要反过来

            carry = cursum // 10

            i-=1 
            j-=1


        if carry !=0:
            res.append(str(carry))
        return "".join(reversed(res)) #使用提供的字符串（在这里是空字符串）作为连接符。"4", "3", "2", "1"会变成 "4321" 


# @lc code=end








