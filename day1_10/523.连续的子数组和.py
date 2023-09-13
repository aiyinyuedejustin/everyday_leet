#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
# https://leetcode.cn/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (28.57%)
# Likes:    536
# Dislikes: 0
# Total Accepted:    99.7K
# Total Submissions: 348.4K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
# 
# 
# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 
# 
# 如果存在，返回 true ；否则，返回 false 。
# 
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
# 
# 示例 2：
# 
# 
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #对比523题，--和为k的子数组-- 前缀和

    # 如果存在一个整数 n ，令整数 x 符合 x = n * k ，
    # 则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。

# 同余定理的应用：
# 如果两个数除以某个数k得到的余数相同，那么这两个数之差可以被k整除。在这个问题中，我们要找的是一个子数组，
# 其和可以被k整除。如果我们在某个位置得到一个前缀和，并且这个前缀和除以k的余数在之前已经出现过，
# 那么这意味着从上次出现这个余数的位置到当前位置的子数组的和可以被k整除。

# eg: sum 到i的时候，除k的余数是3， sum到j的时候除以k的余数也是3，那么从i..j的sum就刚好是k的倍数

# 现在，我们模拟这个代码：

# 假设 nums = [23, 2, 4, 6, 7] 和 k = 6。

# 初始化 dic = {0: -1} 和 cursum = 0。
# 当 index = 0，num = 23，cursum = 23，rem = 23 % 6 = 5。5 不在 dic 中，所以 dic[5] = 0。
# 当 index = 1，num = 2，cursum = 25，rem = 25 % 6 = 1。1 不在 dic 中，所以 dic[1] = 1。
# 当 index = 2，num = 4，cursum = 29，rem = 29 % 6 = 5。5 已经在 dic 中，且 index - dic[5] = 2 > 1，所以返回 True。
# 这意味着从索引0到索引2的子数组 [23, 2, 4] 的和是6的倍数。
       
        dic = collections.defaultdict(int)
        dic[0] = -1  # 存的是某个余数出现的index！！！！初始化为-1，因为对于余数刚好是0的情况，我们要限制一下，看下面
        cursum = 0
        
        for index, num in enumerate(nums):
            cursum += num
            rem = cursum % k
            
            if rem in dic and index - dic[rem] >=2: #index - dic[rem] >=2 为了确保两个index间长度至少2，而560题即使是单个元素也算
                return True
            
            # 只有当rem不在dic中时，我们才更新它，这样我们可以保留rem首次出现的位置，所以一定要用dic[rem] = index,
            # 而不是像560题一样+= 次数，此处我们不管次数，只管有没有出现过
            # 所以一定要有个if，而不是直接不顾一切累加，是只关心第一次出现的index
            if rem not in dic:
                dic[rem] = index
        
        return False

# 为什么初始化dic[0]=-1:是为了处理累加除以k就是0的情况，不然过不了我们>=2的条件
# 对于nums = [3, 3]
# 过程如下：
# Index: 0, Num: 3, CurSum: 3, Rem: 3, Dic: {0: -1, 3: 0}
# Index: 1, Num: 3, CurSum: 6, Rem: 0, Dic: {0: -1, 3: 0}
# True
#如果初始化为dic[0]=0，第二次Rem =0,对于if条件，1-0=1 并不>=2， 然而其实长度够了，因此必须初始化为-1 


#1. 余数定理，有两个数，每个数除以k的余数相同，那么这俩数相减就是k的倍数。因此可以用前缀和。
# cursum_i 除以k的余数 = cursum_j 除以k的余数，那么从 i++++j 就是k的倍数，就是连续子数组
#1. 使用default dict 记录每个余数的第一次的index，为了处理余数刚好等于0的情况，
        # dic = collections.defaultdict(int)
        # dic[0] = -1
        # cursum =0 

        # #为了确保至少长度为2，需要记录当前index
        # for index, num in enumerate(nums):

        #     cursum  += num
        #     rem = cursum % k

        #     if rem in dic and index-dic[rem] >=2:
        #         return True
            
        #     if rem not in dic:
        #         dic[rem] =index

        # return False
    









# @lc code=end

