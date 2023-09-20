#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.82%)
# Likes:    2068
# Dislikes: 0
# Total Accepted:    350.2K
# Total Submissions: 782.1K
# Testcase Example:  '[1,1,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
# 
# 子数组是数组中元素的连续非空序列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3], k = 3
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #使用前缀和

        # nums = [1,1,0,1,2] 和 k = 2

        # 初始化：

        # cur_sum = 0
        # res = 0
        # num_times = {0: 1} (我们从一个前缀和为0的情况开始，因为没有任何元素时的和就是0)
        # 当处理到第一个元素 1 时：

        # cur_sum = 1
        # 检查 1 - 2 = -1 是否在 num_times 中，不在。
        # 更新 num_times，现在 num_times = {0: 1, 1: 1}
        # res 保持为 0
        # 当处理到第二个元素 1 时：

        # cur_sum = 2
        # 检查 2 - 2 = 0 是否在 num_times 中，是的，所以 res 增加 num_times[0]，即 res = 0 + 1 = 1
        # 更新 num_times，现在 num_times = {0: 1, 1: 1, 2: 1}
        # 当处理到第三个元素 0 时：

        # cur_sum 保持为 2 (因为加了0，所以和不变)
        # 检查 2 - 2 = 0 是否在 num_times 中，是的，所以 res 增加 num_times[0]，即 res = 1 + 1 = 2
        # 更新 num_times，但 2 的计数增加了，现在 num_times = {0: 1, 1: 1, 2: 2}
        # 当处理到第四个元素 1 时：

        # cur_sum = 3
        # 检查 3 - 2 = 1 是否在 num_times 中，是的，所以 res 增加 num_times[1]，即 res = 2 + 1 = 3
        # 更新 num_times，现在 num_times = {0: 1, 1: 1, 2: 2, 3: 1}
        # 当处理到第五个元素 2 时：

        # cur_sum = 5
        # 检查 5 - 2 = 3 是否在 num_times 中，是的，所以 res 增加 num_times[3]，即 res = 3 + 1 = 4
        # 更新 num_times，现在 num_times = {0: 1, 1: 1, 2: 2, 3: 1, 5: 1}
        # 最终，res = 4，表示我们找到了4个满足条件的子数组。


        # 如果两个数的差是k，那么其中一个数减去k就是另一个数。

        # 要求的连续子数组
         # num_times 存储某“前缀和”出现的次数，这里用collections.defaultdict来定义它
        # 如果某前缀不在此字典中，那么它对应的次数为0
        # num_times = collections.defaultdict(int)
        # num_times[0] = 1  # 先给定一个初始值，代表前缀和为0的出现了一次
        # cur_sum = 0  # 记录到当前位置的前缀和
        # count = 0
        # for i in range(len(nums)):
        #     cur_sum += nums[i]  # 计算当前前缀和
        #     if cur_sum - k in num_times:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去【之前某一位的前缀和】等于k
        #         #也就是相当于从前面某一位sum，到当前位置刚好是k，中间这段距离的sum=k，那这段就是要找的子数组，所以count+ 上一个前缀和出现的次数
        #         count += num_times[cur_sum - k]
        #     # 下面一句实际上对应两种情况，一种是某cur_sum之前出现过（直接在原来出现的次数上+1即可），
        #     # 另一种是某cur_sum没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果cur_sum这个key不存在将返回默认的int，也就是0）
        #     # 返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
        #     num_times[cur_sum] += 1
        # return count


        


        #需要一个记录每个cursum出现几次的计数器，用defaultdict
        dic = collections.defaultdict(int)
        dic[0] =1 #cursum = 0 初始化为1， 代表开头0开始累积，一次
        cursum = 0 
        count = 0 
         
        for i in range(len(nums)):
            cursum += nums[i]   

            if cursum-k in dic: 
                count += dic[cursum-k]  # 要加上 某个前缀和出现的次数，比如在第1和第5 位的前缀和都是想要的，那么一定要+=2，不然会跳过一些解

        #如果位置j的cursum - 位置i的cursum =k，说明从i加到j刚好是k，找到连续数组
                # 首先，我们明确一下 dic 的作用：它记录了到目前为止，每个前缀和出现的次数。
                # count +=1 这个不对
                #eg[1，-1,0]，k=0, 如果count+=1， 那么第一次找到时i=1，cursum =0, dic=[0:1, 1:1],count+=1 =1. 
                #第二次找到时候i=2， 也就是[1,-1,0]的cursum -k =0, dic = [0:2],coutnt+=1 =2就无了，相当于跳过了【0】这种解
                # 如果是用count+= dic[cursum-k]也就是count+=2, 会直接从上一步count=1 变成3， 因为0 这个cursum出现了2次（一次开头，一次1+ (-1))，不能跳过,不然少结果
                # 当我们在遍历数组时，对于当前位置的前缀和 cursum，我们想知道有多少个之前的位置的前缀和，
                # 使得从那个位置到当前位置的子数组的和为 k。这可以通过检查 cursum - k 是否在 dic 中来实现。
                # 如果 cursum - k 在 dic 中，那么 dic[cursum-k] 就是 cursum - k 这个前缀和出现的次数。
                # 换句话说，有 dic[cursum-k] 个之前的位置，使得从那个位置到当前位置的子数组的和为 k。
                # 因此，我们不仅仅是增加 count 的值1，而是增加 dic[cursum-k] 的值，因为这表示我们找到了 dic[cursum-k] 个
                # 新的满足条件的子数组。
             


            dic[cursum] +=1

        
        return count







  
       



# @lc code=end

