#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (49.63%)
# Likes:    2093
# Dislikes: 0
# Total Accepted:    706.4K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 
# 
# 提示：
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # https://www.youtube.com/watch?v=0Ue1-11HCrs&ab_channel=CrackingFAANG
        # 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
        # intervals[i].length == 2 ,每个interval的lenth都是2
        # 输出：[[1,6],[8,10],[15,18]]
        # 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
        # 注意interval可能不是sorted 比如[[2,6],[1,3],[8,10],[15,18]],我们还是得merge[2,6] 和[1,3]
        # 因此可能要先sort一下
        if len(intervals)<=1:
            return intervals #不合法的先排除，就是只被提供了一个区间， (其实可以不写)
        
        intervals.sort(key = lambda x: x[0]) #sort默认是按照每个元素的第一个值，且start<=end，所以只按照第一个sort即可把所有区间左侧sort了
        
        res = [intervals[0]] #由于interval已经sort，result的第一个就是interval第一个，没有比这个再小的了，初始化为【1，3】

        for start, end in intervals[1:]: #从第二个元素（区间）开始看。这么写可以直接拆包子列表内的元素，合法
            if start <= res[-1][1]: #res[-1][1]指result最后一个元素的第二位，也就是 ‘ start= 2 对比 【1,3】中的3
                #或者说，如果下一个区间的第一位，小于前一个区间的最后一位|此处得加上等于号，不然max没法更新 比如[1,3] [3,4] 应该更新右区间
                # 就应该更新之前区间的右边为：max（之前的右边，现在的右边）
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start,end]) #如果区间不连续，就直接加入，如[8,10]
        return res

# 初始化:

# intervals = [[2,6],[1,3],[8,10],[15,18]]
# 检查 len(intervals) <= 1，这不成立，所以继续执行。
# 排序:

# 执行 intervals.sort() 后，intervals 变为 [[1,3],[2,6],[8,10],[15,18]]。
# 初始化结果列表:

# res = [[1,3]]，因为我们取 intervals 的第一个元素。
# 开始遍历 intervals 从第二个元素开始：

# 当前元素：[2,6]

# start = 2, end = 6
# 检查 start <= res[-1][1]，即 2 <= 3，这成立。
# 执行 res[-1][1] = max(end, res[-1][1])，即 res[-1][1] = max(6, 3) = 6。
# res 更新为 [[1,6]]。

# 当前元素：[8,10]

# start = 8, end = 10
# 检查 start <= res[-1][1]，即 8 <= 6，这不成立。
# 执行 res.append([start, end])，将 [8,10] 添加到 res。
# res 更新为 [[1,6],[8,10]]。

# 当前元素：[15,18]

# start = 15, end = 18
# 检查 start <= res[-1][1]，即 15 <= 10，这不成立。
# 执行 res.append([start, end])，将 [15,18] 添加到 res。
# res 更新为 [[1,6],[8,10],[15,18]]。
# 结束遍历，返回 res，即 [[1,6],[8,10],[15,18]]。


        # #先sort，
        # intervals.sort()

        # # 初始化result为intervals的第一个，因为已经sort不需要让第一个跟之前比较
        # res = [intervals[0]]

        # #从第二个开始，对比第一位。 如果后一个的第一位<=前一个的第一位，那么前一个的右区间更新为max(之前的，现在的)
        # for i in intervals[1:]:
        #     start, end = i[0], i[1]
        #     if start<= res[-1][1]:
        #         res[-1][1] = max(end,res[-1][1])
        #     else:
        #         res.append([start,end])
        # return res



# @lc code=end

