#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.89%)
# Likes:    2737
# Dislikes: 0
# Total Accepted:    777K
# Total Submissions: 1.8M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：nums = [1], target = 0
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2,3,4,5,6,7]-> [4,5,6,7,1,2,3] 会发现在4切完移动完后，是两个从小到大的 数组
        #普通二分搜索，(l+r)//2 = m， 然后比较nums[m] 和target
        #但在这里我们不能这样

        #step：
        #1. 切完后[4,5,6,7,1,2,3] ， 初始m是7,，先看m是不是target,是的话ok

        # 2. 先看if l<m，说明左半部分排序好了。那就先看左半部分。再看右半部分
        # 2.1 那先看l是不是target， 是的话返回。
        # 2.2 不然看target是不是夹在左半部分中： [l<target<m]。说明target夹在4567中，如果是的话，更新right= m-1，(m都比target大了)

        # 2.3 如果2.2不成立，说明在右半部分sort的array中，直接更新l到m+1继续即可


        #3. 如果左半部分没排序好，直接先去右半部分，再看左半部分
        # 3.1 看r 是不是target，此时r=3,因为在4切得，所以3其实也是切点，会被放在最右边。是的话直接return
        #3.2 如果如果r不是target，那就看 [m <target <r]。说明目标夹在123中，直接更新 l = m+1(对右半部分普通二分搜索)
        # 3.3 如果不在区间，说明还在左半部分，r =m-1下一轮while就会搜索没排序好的左半部分。

        # 
        # 如果在的话继续上面的逻辑,更新l=m+1（m都比target小了。直接把l移到右半部分开头）
        # 如果还不成立，说明数组根本没有target， return -1
        l = 0 
        r = len(nums)-1

        while l<= r: #bin search
            m = (r+l)//2 

            if nums[m] == target:
                return m #如果第一轮m就达到了，直接stop
            
            elif nums[l] < nums[m]: #检查左半部分是否排序好，
                # 如：[4,5,6,7|,0,1,2]可以，但是[7,0,1,2,3,4,5]他就不是
                #如果排序好，那就继续看：
                if nums[l] == target:
                    return l
                elif nums[l] <target< nums[m]:
                    r = m -1 #进行下一个while，继续从上往下执行，相当于前面已经写好了二分搜索
                else:
                    l = m+1 #不然的话，说明不在左半部分，要去右半部分看了，l更新，下一轮while还是执行这个elif，只是范围到了右半部分

            else: #如果左半部分没有排序好，直接往右半边看，如[7,0,1,2,3,4,5]的右半部分是0-5
                if nums[r]==target: #先看r是不是
                    return r
                elif nums[m]<target<nums[r]: #看在不在右半部分，在的话，l要m+1
                    l = m+1
                else: #不然表示往低处搜。 注意这个else跟外层上一个 elif的else不是同一个意思。这里的这个else自己实现了一个二分搜索
                    r = m -1
        return -1 
    


# [7,0,1,2,3,4,5], the target value 0：

# 开始时：

# Left boundary (l) is at index 0.
# Right boundary (r) is at index 6.
# We calculate the midpoint: m = (0 + 6) // 2 = 3.
# We inspect the values: nums[0] is 7, nums[3] is 2, and nums[6] is 5.
# Since the left half (from 7 to 2) is not sorted, our code moves into the else block. 
# The right half (from 2 to 5) is sorted,
#  but our target value 0 is not within this range. So,
#  we narrow down our search to the left half by setting r to m - 1=3-1=2.

# In the second iteration: 

# Left boundary (l) remains at index 0.
# Right boundary (r) is now at index 2.
# We calculate the new midpoint: m = (0 + 2) // 2 = 1.
# We inspect the values: nums[0] is 7, nums[1] is 0, and nums[2] is 1.
# Now, we see that nums[1] is our target value 0. So, the function returns index 1.
#     #     return -1 
                     
            

# @lc code=end

