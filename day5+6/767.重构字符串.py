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
        # https://www.youtube.com/watch?v=2g_b1aYTHeg&t=850s&ab_channel=NeetCode
        # 返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。

        # start from the most frequence charater
 

        # 还是用maxHeap,  ---O(nlogn)
        # 跟之前一个题比较像 --621 task scheduler, 从最frequent开始
        #
        # eg : 先计算每个字母的次数： a:3 b:1 c:1 
        # 一开始a是most frequent,因此-> [a] 
        # a剩2次，下一位要用除了a的最多次的， 可以任意b or c : -> [a,b]
        # b 剩一次，下一位用除了b最多的 -> [a,b,c]
        # 走到最后： [abaca] done！

        #python 没有max heap，我们先变成负的即可
        #需要一个东西，记录上一次用了哪个字母，下一次不能再用


        count = Counter(s) #次数
# s = 'abbccc'
# res = Counter(s)
#  #Counter({'c': 3, 'b': 2, 'a': 1}) 是个dict

        maxHeap = [[-cnt,char] for char,cnt in count.items()] 
        #变成负的--[-cnt,char] 是为了给heapify排序用（默认第一位），这里调换顺序ok的。 为什么保留char--因为还要添加用
        heapq.heapify(maxHeap) #初始化min heap structure,但由于是负的，最大值会在前面变成max heap

        prev = None  #记录之前用的哪个，下一次不能重复用了
        res = '' #初始化empty list

        while maxHeap or prev:
            # edge case : a:3次， b:1次; 过了3次loop之后，
            # res ='aba' ， maxheap=[], prev = [1,a].这个时候我们不能再添加了，这就是停止条件（真难想）
            #
            if prev and not maxHeap: #maxheap空了，prev不是空，就说明不行
                #其实也可以理解为，当除了most freq的元素都用完了（maxheap null)，
                # 但most freq还剩下，你下面几轮，只能添加n个相同的元素，那这就不符合adjacent不相同
                return ""

            #most freq, expect prev
            cnt,char =   heapq.heappop(maxHeap) #first most frequent--a
            res+=char #直接加入res

            cnt +=1 #降低次数（次数是负的，+是往0走)


            # 一定先写这个if，不然cnt!=0 就把prev 覆盖了，但我们还没用这个prev
            if prev: #如果当前prev not null ,我们下一次应该先用prev，就像是aaabc, 
                # 先用了一次a，prev=a, 然后b，然后继续a而不是c，我们不能直接对prev覆盖了，永远要先用most freq
                heapq.heappush(maxHeap,prev)
                prev =None # set back to None


            #一定后写这个if，不然会把前面的prev 覆盖，但我们还没用第二个a
            if cnt !=0: #如果还剩下次数，我们才记录上一次用了啥，不然他都没了，也不可能下一次继续用了
                prev = [cnt,char] #记录当前用了啥

            
        return res






# @lc code=end

