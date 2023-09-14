#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.55%)
# Likes:    2470
# Dislikes: 0
# Total Accepted:    848.7K
# Total Submissions: 2M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 是一个非递减数组
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # https://www.youtube.com/watch?v=4sQL7R5ySUU&ab_channel=NeetCode
        # 用logn time的 --- 即使两次binary search 也是logn
        #binary search 二分搜索
        # 左右指针 , 
        # left +right/2即 middle， 用middle对比target， 大了就把right往做，小了就把left往右


        #特殊case: 577 888；left在第一个8，如果right 在最右边，middle是第二个8，我们就停了，但其实我们想要right most index
        # 改进binary search： 
        #1. 先找right，，从之前的地方继续寻找，把left扔到最右边的8跟right对齐，即m+1，看看是不是8，且是不是最后一个。那么right index找到了
        #2. 再找left： restart binary search. left，middle和right还是停在888这个位置。此时把right扔到left的位置，即mid-1
        left = self.binSearch(nums,target,True) #
        right = self.binSearch(nums,target, False)
        return [left,right] #true false包含了

    def binSearch(self,nums,target, leftBias): #helper function. leftBias是true false，
        #如果是 false就代表rightBias，也就是577888这种感觉的， 也就找rightmost index.
        # 如果是True就是寻找leftmost index
        l,r = 0, len(nums)-1 
        i = -1 #存储middle的index，初始化为-1，为了满足找不到就不更新i，return i=-1
        while l<=r:
            m = (l+r)//2
            if nums[m] < target:#小了，l移动到m，因为m都比这个小，下一个至少得是m+1
                l = m+1
            elif nums[m] > target:
                r = m-1
            else: #find a target
                i = m  #更新middled值，也就是用于代表left或者rightmost的index的值，要一直更新这个
                #一定要赶在leftBias前更新i，这样到最后l>r前，i刚好落在最左侧或者最右侧
                if leftBias: #改进bin search，如果目前找的是leftmost index, 应该把right移动到left，也就是m-1
                    r = m-1 #更新完会再次循环，确保确实是left most bia 
                else:#如果目前找的是rightmost index, 应该把left移动到right，也就是m+1
                    l = m+1
        return i 
    


# 给定的数组：nums = [5,7,7,8,8,8] 和 target = 8。

# 第一次调用binSearch（寻找起始位置）：

# 初始化：l=0, r=5, i=-1
# 第一次循环：m=2, nums[2]=7 < 8，所以l=3
# 第二次循环：m=4, nums[4]=8 == 8，因为leftBias=True，所以r=3，并且i=4
# 第三次循环：m=3, nums[3]=8 == 8，因为leftBias=True，所以r=2，并且i=3
# 退出循环，返回i=3
# 第二次调用binSearch（寻找结束位置）：

# 初始化：l=0, r=5, i=-1
# 第一次循环：m=2, nums[2]=7 < 8，所以l=3
# 第二次循环：m=4, nums[4]=8 == 8，因为leftBias=False，所以l=5，并且i=4
# 第三次循环：m=5, nums[5]=8 == 8，因为leftBias=False，所以l=6（此时l超出了数组的范围，但这不是问题，因为我们只是用它来判断循环是否应该继续），并且i=5
# 退出循环，返回i=5
# 最后，searchRange函数返回[3,5]，这是目标值8在数组中的起始和结束位置。
# @lc code=end

