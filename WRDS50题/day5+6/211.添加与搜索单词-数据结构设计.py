#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode.cn/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (49.63%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    76.1K
# Total Submissions: 153.4K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 
# 实现词典类 WordDictionary ：
# 
# 
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些
# '.' ，每个 . 都可以表示任何一个字母。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# 
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // 返回 False
# wordDictionary.search("bad"); // 返回 True
# wordDictionary.search(".ad"); // 返回 True
# wordDictionary.search("b.."); // 返回 True
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= word.length <= 25
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最多调用 10^4 次 addWord 和 search
# 
# 
#

# @lc code=start
class WordDictionary:

    def __init__(self):


    def addWord(self, word: str) -> None:


    def search(self, word: str) -> bool:



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

