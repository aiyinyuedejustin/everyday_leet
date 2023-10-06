#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode.cn/problems/word-break-ii/description/
#
# algorithms
# Hard (57.56%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    92.3K
# Total Submissions: 160.2K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序
# 返回所有这些可能的句子。
# 
# 注意：词典中的同一个单词可能在分段中被重复使用多次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# 输出:["cats and dog","cat sand dog"]
# 
# 
# 示例 2：
# 
# 
# 输入:s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# 输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 
# 输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# 输出:[]
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中所有字符串都 不同
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #继承自word break1 --- 139
        # https://www.youtube.com/watch?v=8DV-cXg6Rh0&ab_channel=CrackingFAANG

        # DFS+memo

        # 搜索知道""" empty string

        # memo = {} #用于存储已经搜索过得 可以不要

        def dfs(string):
            # if string in memo: #如果已经搜索过，直接return，免得再次搜索
            #     return memo[string]
            if not string: #如果string是empty list ”“
                return [''] #return 一个empty string，说明我们已经搜索完了可以构成句子
            #for sub_word in sub_words: 这句话必须是可迭代对象，如果只是return empty string， 这个没法操作，报错，所以只能list of empty string，这样
            #for 出来也还是空的，是可以保证下面的能正常运行
            
            local_res = [] #切割到最后og，如果切割不了，return的一直都是空的local res，所以最终return到最外层也还算空的。这会导致下面的sub_words一直是[]
            #因此最后return也是空，能过得了切不干净的case

            for word in wordDict:
                if string.startswith(word):
                    #此处sub_word是第一次split后剩余的部分继续搜索切分成的word， 会是一个list，因为递归
                    sub_words =dfs(string[len(word):]) #递归继续搜索剩余的能不能被词典中的分开，直到一个empty string
                    #eg. catsanddog , word= cat, 于是第一次从cat切开, 对sandog再次调用dfs， 最终会返回sub_words = [’sand dog' ]
                    #注意这里切干净的时候最后会有个empty tring

                    # add space 
                    for sub_word in sub_words:
                        #" " if sub_word else "" 是因为最后切干净了会剩下"" , 但我们不会对empty string后面再加个space，
                        # 不然就变成了"cat and dog空格" 而不是"cat and dog"。 所以要排除empty string
                        local_res.append(word + (" " if sub_word else "") + sub_word) # cat+ _sand+ _dog 
            # memo[string] = local_res

            return local_res #递归完了这里面就是所有的sub_words， 
        
        return dfs(s)
    

# O（2



# 调用 dfs("catsanddog"):

# string = "catsanddog"
# local_res = []
# 对于 word = "cat":

# string.startswith("cat") 是 True
# 调用 dfs("sanddog"):
# string = "sanddog"
# local_res = []
# 对于 word = "sand":
# string.startswith("sand") 是 True
# 调用 dfs("dog"):
# string = "dog"
# local_res = []
# 对于 word = "dog":
# string.startswith("dog") 是 True
# 调用 dfs(""):
# string = ""
# 返回 ['']
# sub_words = ['']
# local_res = ["dog"]
# memo["dog"] = ["dog"]
# 返回 ["dog"]
# sub_words = ["dog"]
# local_res = ["sand dog"]
# memo["sanddog"] = ["sand dog"]
# 返回 ["sand dog"]
# sub_words = ["sand dog"]
# local_res = ["cat sand dog"]
# 对于 word = "cats":

# string.startswith("cats") 是 True
# 调用 dfs("anddog"):
# string = "anddog"
# local_res = []
# 对于 word = "and":
# string.startswith("and") 是 True
# 调用 dfs("dog"):
# 由于我们之前已经计算过 dfs("dog")，我们可以直接从 memo 中获取结果，即 ["dog"]
# sub_words = ["dog"]
# local_res = ["and dog"]
# memo["anddog"] = ["and dog"]
# 返回 ["and dog"]
# sub_words = ["and dog"]
# local_res = ["cat sand dog", "cats and dog"]
# 对于其他单词，它们不会匹配 "catsanddog" 的开头，所以我们不需要再继续模拟。

# memo["catsanddog"] = ["cat sand dog", "cats and dog"]

# 返回 ["cat sand dog", "cats and dog"]
        




    
# @lc code=end

