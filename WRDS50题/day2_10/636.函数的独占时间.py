#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#
# https://leetcode.cn/problems/exclusive-time-of-functions/description/
#
# algorithms
# Medium (66.11%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    35.8K
# Total Submissions: 54.1K
# Testcase Example:  '2\n["0:start:0","1:start:2","1:end:5","0:end:6"]'
#
# 有一个 单线程 CPU 正在运行一个含有 n 道函数的程序。每道函数都有一个位于  0 和 n-1 之间的唯一标识符。
# 
# 函数调用 存储在一个 调用栈 上 ：当一个函数调用开始时，它的标识符将会推入栈中。而当一个函数调用结束时，它的标识符将会从栈中弹出。标识符位于栈顶的函数是
# 当前正在执行的函数 。每当一个函数开始或者结束时，将会记录一条日志，包括函数标识符、是开始还是结束、以及相应的时间戳。
# 
# 给你一个由日志组成的列表 logs ，其中 logs[i] 表示第 i 条日志消息，该消息是一个按 "{function_id}:{"start" |
# "end"}:{timestamp}" 进行格式化的字符串。例如，"0:start:3" 意味着标识符为 0 的函数调用在时间戳 3 的 起始开始执行
# ；而 "1:end:2" 意味着标识符为 1 的函数调用在时间戳 2 的 末尾结束执行。注意，函数可以 调用多次，可能存在递归调用 。
# 
# 函数的 独占时间
# 定义是在这个函数在程序所有函数调用中执行时间的总和，调用其他函数花费的时间不算该函数的独占时间。例如，如果一个函数被调用两次，一次调用执行 2
# 单位时间，另一次调用执行 1 单位时间，那么该函数的 独占时间 为 2 + 1 = 3 。
# 
# 以数组形式返回每个函数的 独占时间 ，其中第 i 个下标对应的值表示标识符 i 的函数的独占时间。
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# 输出：[3,4]
# 解释：
# 函数 0 在时间戳 0 的起始开始执行，执行 2 个单位时间，于时间戳 1 的末尾结束执行。 
# 函数 1 在时间戳 2 的起始开始执行，执行 4 个单位时间，于时间戳 5 的末尾结束执行。 
# 函数 0 在时间戳 6 的开始恢复执行，执行 1 个单位时间。 
# 所以函数 0 总共执行 2 + 1 = 3 个单位时间，函数 1 总共执行 4 个单位时间。 
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1, logs =
# ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
# 输出：[8]
# 解释：
# 函数 0 在时间戳 0 的起始开始执行，执行 2 个单位时间，并递归调用它自身。
# 函数 0（递归调用）在时间戳 2 的起始开始执行，执行 4 个单位时间。
# 函数 0（初始调用）恢复执行，并立刻再次调用它自身。
# 函数 0（第二次递归调用）在时间戳 6 的起始开始执行，执行 1 个单位时间。
# 函数 0（初始调用）在时间戳 7 的起始恢复执行，执行 1 个单位时间。
# 所以函数 0 总共执行 2 + 4 + 1 + 1 = 8 个单位时间。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 2, logs =
# ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
# 输出：[7,1]
# 解释：
# 函数 0 在时间戳 0 的起始开始执行，执行 2 个单位时间，并递归调用它自身。
# 函数 0（递归调用）在时间戳 2 的起始开始执行，执行 4 个单位时间。
# 函数 0（初始调用）恢复执行，并立刻调用函数 1 。
# 函数 1在时间戳 6 的起始开始执行，执行 1 个单位时间，于时间戳 6 的末尾结束执行。
# 函数 0（初始调用）在时间戳 7 的起始恢复执行，执行 1 个单位时间，于时间戳 7 的末尾结束执行。
# 所以函数 0 总共执行 2 + 4 + 1 = 7 个单位时间，函数 1 总共执行 1 个单位时间。 
# 
# 示例 4：
# 
# 
# 输入：n = 2, logs =
# ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
# 输出：[8,1]
# 
# 
# 示例 5：
# 
# 
# 输入：n = 1, logs = ["0:start:0","0:end:0"]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 0 
# 0 
# 两个开始事件不会在同一时间戳发生
# 两个结束事件不会在同一时间戳发生
# 每道函数都有一个对应 "start" 日志的 "end" 日志
# 
# 
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        #https://www.youtube.com/watch?v=CBJI_lZxYU8&ab_channel=CrackingFAANG
        #  n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
        #注意这题 func0 start at 0 ,因为单线程，func2 start at 2 的时候，func0运行了2秒
        #但是func1 end at 5指的是在5分钟的最后，也就是第6分开始的时候end的。然后func0 end 6其实是运行了6-7一整秒
        # 此处因为单线程，所以同时只能运行一个程序。用了stack的概念，如果start 我们就push to stack, 如果end，我们pop the stack，计算delta
        # 注意end at 5,是end inclusive,其实是6的开头end的， 要+1


#         在Python中，当我们使用列表作为栈时：

# “栈顶”是列表的最后一个元素。
# “栈底”是列表的第一个元素。
# 因此，当我们说“堆顶元素”或“栈顶元素”时，我们指的是列表的最后一个元素。我们使用 list[-1] 来访问它，
# 使用 list.append(item) 来将一个元素推入栈顶，使用 list.pop() 来从栈顶弹出一个元素。

        #注意top of the stack就是currently running的func
        # 用array store result
        execution_times = [0]*n #保存每个func最终的累计运行时间 ,list（其中第 i 个下标对应的值表示标识符 i 的函数的独占时间。）
        call_stack = [] #也用list，用来存储运行的func的id（也是index）
        prev_start_time = 0 #初始化每个func的前一个开始的时间，用于计算时间差

        for log in logs:
            #先parse出来信息
            func_id, call_type, timestamp = log.split(':')
            func_id = int(func_id) #convert to int 
            timestamp = int(timestamp) #convert to int 
            
            if call_type == 'start': #如果是start，我们就加入stack
                if call_stack: # 但如果之前stack里有东西，说明之前有个func还在运行，要停止但不用删除因为他还没end，因为单线程。只需count上一个func运行的时间
                    # call_stack[-1] 是index，第一次循环代表index0 
                    # 这只是访问栈顶的元素，不会从栈中删除它。
                    # 它等效于查看栈顶的元素（正在运行的），但不移除它。
                    # 如果栈是空的，这会引发一个错误 #stack[-1]就是堆顶的那个
                    execution_times[call_stack[-1]] += timestamp -prev_start_time #prev_start_time是上个函数开始的时间
                
                call_stack.append(func_id) #现在的func id 加入stack,这个id刚好是从0开始的，可以当index用
                prev_start_time = timestamp #新func的新的start time更新
            else: #如果是end
                #call_stack.pop()删除call_stack中堆顶，因为end了），同时返回index，刚好对应上excu里面目前end 的func的位置，更新他的时间
                # call_stack.pop():
                # 这会移除并返回栈顶的元素。
                # 这是一个修改栈的操作，因为它实际上从栈中删除了一个元素。
                # 如果栈是空的，这也会引发一个错误
                execution_times[call_stack.pop()] += timestamp - prev_start_time+1 #注意end at 5,是end inclusive,其实是6的开头end的， 要+1
                
                prev_start_time = timestamp + 1 #此func结束了，下一个func要继续了，那就更新下一个函数运行开始的时间，注意是end at 6,所以还是5+1
        return execution_times

# O（N
# O(N)

# @lc code=end

