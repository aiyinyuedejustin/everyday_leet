#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (37.30%)
# Likes:    6318
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 
# 你返回所有和为 0 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #用双指针（其实是i，left， right三个指针）双指针一定要排序。 此题一定要对i left right三个都去重
        result = []
        nums.sort() 
        
        for i in range(len(nums)):#对每个i遍历
            # 1. 如果第一个元素已经大于0，因为已经排序过，那么不可能还有3个数sum=0，
            # 这里写return result，或者break都行，因为就是最外层循环。在四数之和那边第二层循环写return result不对
            if nums[i] > 0:
                break
            
            # 2. 对i去重：不能使用if i > 0 and nums[i] == nums[i + 1]: 或 if nums[i] == nums[i + 1]:
            
            if i > 0 and nums[i] == nums[i - 1]:
                # 使用 `if i > 0 and nums[i] == nums[i - 1]: continue` 是为了对i去重。避免重复的三元组。
                # 1. `i > 0` 确保我们不会在 i=0 时进行比较，这样就避免了与数组最后一个元素进行不必要的比较。
                # 2. `nums[i] == nums[i - 1]` 确保当前元素与前一个元素不同，以避免重复。如[-1, 0, 0, 1, 1]会去掉第二个0和第二个1

                # 如果仅使用 `if nums[i] == nums[i - 1]: continue`，在某些特殊情况（如 [0,0,0]）下，
                # 会导致第一个元素与数组最后一个元素比较，从而可能跳过第一个i=0,left=0,right=0,错失有效的三元组[0,0,0]

                # 如果使用 `if i > 0 and nums[i] == nums[i + 1]: continue` 或 `if nums[i] == nums[i + 1]: continue`，
                # 则可能会跳过某些有效的三元组，因为它只检查了当前元素与下一个元素。如[-1, 0, 0, 1]，有效的是[-1,0,1]，而0会被跳过，从而输出[null]

                continue           #[-2, -1, -1, 0, 1, 1, 2]
                
            left = i + 1 #left设置为当前i的右侧
            right = len(nums) - 1 #right永远在末尾
            
            while right > left: #如果right<left了，那就重复计数i右侧的数字了，没意义
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:#此时三数之和小，left向右（排序过）
                    left += 1
                elif sum_ > 0:#此时三数之和大，right向左
                    right -= 1
                else:#此时三数之和=0
                    result.append([nums[i], nums[left], nums[right]]) 
                    
                    # 3. 对left right去重 ，应该同时移动
                    # 3.1去重逻辑应该放在找到一个三元组之后，如【0,0,0,0，0】如果把去重逻辑放在外层while right>left,你结果都还没保存呢指针就动了，最终啥也没有
                    # e.g. [-1,-1,-1,0,0,1,1,1,2],第一组合法解是[-1,-1,2]. i还是=-1， left最终移动到0，righ移动到1（同时收缩，看下面）。又找到了
                    # 3.2 注意这个while nums[right] == nums[right - 1]:一定要带个right>left，
                    # 如[0,0,0]收货第一组[0,0,0]后， 不加right>left，最终right会从index 2 一直落到-inf,就out of range了
                    # 他还是内圈循环，right会 
                    while right>left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                        
                    #去重只是去重，还是移动到重复的元素的最后一个，还是得继续收缩。
                    #4. 为什么同时移动left和right
                    # 由于数组已排序，所以当 nums[i] + nums[left] + nums[right] == 0 成立时，nums[left] 和 nums[right] 是在当前 i 下唯一能使三元组和为零的配对。
                    # 这是因为数组是有序的，所以不存在其他的 left 和 right 使得三元组和为零。
                    # # 我们使用 while 循环来跳过所有重复的 nums[left] 和 nums[right]。这确保了每个三元组都是唯一的。
                    # # 当找到一个有效的三元组后，我们同时移动 left 和 right 指针以寻找下一个可能的三元组。
                    # 由于我们已经处理了所有可能的 left 和 right（通过 while 循环），所以这样做是安全的。
                    right -= 1
                    left += 1
                    
        return result
# @lc code=end

