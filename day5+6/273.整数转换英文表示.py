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
        mapping = {
          1000000000: 'Billion',
          1000000: 'Million',
          1000: 'Thousand',
          100: 'Hundred',
          90: 'Ninety',
          80: 'Eighty',
          70: 'Seventy',
          60: 'Sixty',
          50: 'Fifty',
          40: 'Forty',
          30: 'Thirty',
          20: 'Twenty',
          19: 'Nineteen',
          18: 'Eighteen',
          17: 'Seventeen',
          16: 'Sixteen',
          15: 'Fifteen',
          14: 'Fourteen',
          13: 'Thirteen',
          12: 'Twelve',
          11: 'Eleven',
          10: 'Ten',
          9: 'Nine',
          8: 'Eight',
          7: 'Seven',
          6: 'Six',
          5: 'Five',
          4: 'Four',
          3: 'Three',
          2: 'Two',
          1: 'One'
        }
        if num==0: #给的是0，直接不干了
            return "Zero"
        result=""
        
        for value, name in mapping.items():
            count=0 #用于存储当前 value 可以完全被 num 整除的次数。
            if num>=value:
               count=num//value #几倍整除（进 1/2/3之类的）
               num = num% value #余数（num应该被更新为剩下的

               #开始往res里面加东西，但是分情况
               if  value>=100: #大于一百就需要更详细的描述，需要 x hundred里面的x，而不像是100以下都很具体
                   result= result+" "+self.numberToWords(count)+" "+name #self.numberToWords(count)是为了返回 x million里面的x。count就是有几个carry
               else:
                   result+=" "+name
        result=result[1:] #循环完了去除开头空格
        # 在这个函数中，每次向 result 字符串添加一个新的单词时，都会在其前面加一个空格。
        # 这是为了确保所有单词之间都有一个空格。但这样做的副作用是，最初的空格会被添加到 result 的开头。
        # 例如，如果 result 是 " One Billion Two Hundred Thirty Four"，那么它将以一个空格开头。
        # 因此，result = result[1:] 是用来去除这个开头的空格的，使得输出格式正确。
        return result
    
# 空间复杂度也是 O(log N)。

# 当然可以，我们可以逐步模拟 `numberToWords` 函数是如何处理输入 `1234567` 的。

# 1. **初始化阶段**: 
#     - `num = 1234567`
#     - `result = ""`（一个空字符串）

# 2. **第一次循环**（针对 `1000000: 'Million'`）:
#     - `count = 1234567 // 1000000 = 1`
#     - `num = 1234567 % 1000000 = 234567`
#     - `count = 1`，而且 `value = 1000000 >= 100`，所以递归调用 `self.numberToWords(count)`，它返回 "One"。
#     - `result = " One Million"`

# 3. **第二次循环**（针对 `100000: 'Hundred Thousand'`）:
#     - `count = 0`（因为 `num < 100000`）
#     - `num = 234567`（没有变化）
#     - 什么都不做。

# 4. **第三次循环**（针对 `1000: 'Thousand'`）:
#     - `count = 234567 // 1000 = 234`
#     - `num = 234567 % 1000 = 567`
#     - `count = 234`，`value = 1000 >= 100`，所以递归调用 `self.numberToWords(234)`，它返回 "Two Hundred Thirty Four"。
#     - `result = " One Million Two Hundred Thirty Four Thousand"`

# 5. **第四次循环**（针对 `100: 'Hundred'`）:
#     - `count = 567 // 100 = 5`
#     - `num = 567 % 100 = 67`
#     - `count = 5`，`value = 100 >= 100`，所以递归调用 `self.numberToWords(5)`，它返回 "Five"。
#     - `result = " One Million Two Hundred Thirty Four Thousand Five Hundred"`

# 6. **第五次循环**（针对 `90: 'Ninety'`）:
#     - `count = 0`（因为 `num < 90`）
#     - `num = 67`（没有变化）
#     - 什么都不做。

# 7. **第六次循环**（针对 `60: 'Sixty'`）:
#     - `count = 67 // 60 = 1`
#     - `num = 67 % 60 = 7`
#     - `count = 1`，`value < 100`，所以直接添加 "Sixty"。
#     - `result = " One Million Two Hundred Thirty Four Thousand Five Hundred Sixty"`

# 8. **第七次循环**（针对 `7: 'Seven'`）:
#     - `count = 7 // 7 = 1`
#     - `num = 7 % 7 = 0`
#     - `count = 1`，`value < 100`，所以直接添加 "Seven"。
#     - `result = " One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`

# 9. **去除开头的空格**:
#     - `result = result[1:] = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`

# 最终输出是 "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"，与预期相符。
    

# @lc code=end

