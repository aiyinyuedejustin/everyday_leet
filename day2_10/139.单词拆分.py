#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode.cn/problems/word-break/description/
#
# algorithms
# Medium (54.38%)
# Likes:    2283
# Dislikes: 0
# Total Accepted:    480.7K
# Total Submissions: 883.8K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
# 
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 
# 
# 示例 2：
# 
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅由小写英文字母组成
# wordDict 中的所有字符串 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #受不了了，不用dp，直接bf
        #https://www.youtube.com/watch?v=CUMRilS83fE&ab_channel=CrackingFAANG

        # BFS， 如 s = "leetcode", wordDict = ["leet", "code"]。
        # 根据wordDict尝试split s， 之后 再次检查。可以知道从t后面分开
        # eg s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
        # 先分cats，然后 and, 剩一个og，不太行。如果分cat，然后sand，然后og，还是不行。这让我们把og过了两遍
        #为了避免，应该用set，避免重复，使用一个visited set。如果之前遇到过，就不搞了，省时间 
        queue =  collections.deque([s]) #会加入整个str
        #collections.deque([s]) 的意思是创建一个 deque 对象并初始化它，使其包含一个元素，即字符串 s。
        #使用 deque 主要是为了实现广度优先搜索（BFS）

        visited = set() 
        while queue:
            word = queue.popleft() #popleft() removes an element from the left side of the deque and returns the value.
            #先检查word 在不在visited set，如果有，就跳过，避免重复
            if word in visited: #如果word 在visited整个都跳过，进行下一个while，我们不想重复做（不过一般continue跳过else就到了while，这个时候queue已经空了，直接return False
                continue
            else: #如果不在，先检查word是不是空的，（str可以被wordDict里面的每一个很好的切分，最后剩empty
                if not word: #到最后全部用完了，如果是空的，就True。 "" 也可以代表False
                    return True
            
                visited.add(word) #set.add() #不在的话就加入
                
                for start_word in wordDict: #对于dict里面的word，看看word是不是start with 某个
                    if word.startswith(start_word):
                        queue.append(word[len(start_word):]) #把剩余的不匹配的加入，下一轮再次处理
        return False #queue 在exhaust后，说明都visite了，说明没法匹配
    
# O（n^3)
# O（n)
# s = "applepenapple"
# wordDict = ["apple", "pen"]



# 开始模拟：

# word = queue.popleft()，所以 word = "applepenapple", queue里面空了因为pop left
# 检查 word 是否在 visited 中。它不在，所以执行else。
# 检查 word 是否为空。它不是，所以继续
# 将 word 添加到 visited 中。现在，visited = {"applepenapple"}
# 遍历 wordDict，检查 word 是否以 wordDict 中的某个单词开头。
# word = "applepenapple"以 "apple" 开头，所以将 word[len("apple"):]，即 "penapple"，添加到 queue 中。现在，queue = ["penapple"]
# 下一轮迭代：

# word = queue.popleft()，所以 word = "penapple"， queue又空了
# 检查 word 是否在 visited 中。它不在，所以继续。
# 检查 word 是否为空。它不是，所以继续。
# 将 word 添加到 visited 中。现在，visited = {"applepenapple", "penapple"}
# 遍历 wordDict，检查 word 是否以 wordDict 中的某个单词开头。
# word 以 "pen" 开头，所以将 word[len("pen"):]，即 "apple"，添加到 queue 中。现在，queue = ["apple"]
# 下一轮迭代：

# word = queue.popleft()，所以 word = "apple" queue又空了
# 检查 word 是否在 visited 中。它不在，所以继续。
# 检查 word 是否为空。它不是，所以继续。
# 将 word 添加到 visited 中。现在，visited = {"applepenapple", "penapple", "apple"}
# 遍历 wordDict，检查 word 是否以 wordDict 中的某个单词开头。
# word 以 "apple" 开头，所以将 word[len("apple"):]，即空字符串，添加到 queue 中。现在，queue = [""]
# 下一轮迭代：

# word = queue.popleft()，所以 word = "" ， queue又空了
# 检查 word 是否在 visited 中。它不在，所以继续。
# 检查 word 是否为空。它是，所以返回 True。
# 因此，对于这个输入，算法返回 True。






# @lc code=end

