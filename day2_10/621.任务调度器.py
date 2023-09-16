#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
# https://leetcode.cn/problems/task-scheduler/description/
#
# algorithms
# Medium (59.84%)
# Likes:    1188
# Dislikes: 0
# Total Accepted:    143.9K
# Total Submissions: 240.4K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1
# 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
# 
# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 
# 你需要计算完成所有任务所需要的 最短时间 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
# ⁠    在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
# 
# 示例 2：
# 
# 
# 输入：tasks = ["A","A","A","B","B","B"], n = 0
# 输出：6
# 解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# 诸如此类
# 
# 
# 示例 3：
# 
# 
# 输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# 输出：16
# 解释：一种可能的解决方案是：
# ⁠    A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A ->
# (待命) -> (待命) -> A
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# tasks[i] 是大写英文字母
# n 的取值范围为 [0, 100]
# 
# 
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # https://www.youtube.com/watch?v=C931gA75CoE&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
        #n代表每一步走完后的冷却数量
        #["A","A","A","B","B","B"] n=2 应该按照：
        # A -> B -> (待命) -> A -> B -> (待命) -> A -> B （n=2）来执行。 因为A走完后要cooldown2次，第一次给B了，但还没完全冷却，
        # 因此B之后还要再等一次才能继续A。 也就是相邻两个A之间必须休息2次。那么B的cooldown 在第二次A后也好了，所以直接连上B  
        # 以此类推



        #重点L：
        # 1、 数量最多的task先走，因为可以走的步数最多
        # 2. A每走一步，就会加上n的冷却时间，其实有n+1步数，如n=2时， A _ _A才合法
        #开始：
        # 3. 要计算一个list，里面存每个task的count，就知道谁最多，让他先走
        # 4. 用一个max heap，自动排序，把刚刚的list加入，把最大的放到最前面，每次pop出来的都会是最大的那个先走
        # 5. 遍历max heap，开始走。要把maxheap 里面的东西pop掉，要判断这个值-1 是不是0. 如果不是0 还可以再走一次，
        # 6. 还需要一个暂时的list，用来放从maxheap pop出来的task并且计算剩余步数
        # 7. 如果maxheap 空，暂时用于存储剩余步数的list也空，就可以return已经走的步数



        #https://www.youtube.com/watch?v=s8p8ukTyA2I&ab_channel=NeetCode 用的这个
        count = Counter(tasks) #数每个task的步数，['A', 'A', 'B', 'C', 'A', 'B']变成{'A': 3, 'B': 2, 'C': 1}
        # 数量最多的先走,这样可以在他冷却的时候process 其他的，省时间
        maxHeap = [-cnt for cnt in count.values()] #由于python的heap默认是minheap，我们要加个负号，这样-3就在最顶端
        #maxHeap = [-3, -3, -1]
        heapq.heapify(maxHeap) #将列表转换为堆。 注意这个必须要heapify，因为虽然negate了，但不一定有那个structure。后面会报错

        time = 0 #初始化总时间
        q = deque() #不传入东西也无所谓 # pairs of [-cnt, time_available] 初始化一个空的双端队列来存储某任务，剩余的cnt和time it becomes available
        while maxHeap or q: #这两个任意一个不空，说明task还没完，我们中间会把task的剩余count从maxHeap扔到q，继续处理
            time += 1 #当开始处理第一个的时候，timey已经花了1unit

            if maxHeap: #maxHeap不空，我们从maxheap拿出开头那个‘最大的’ 由于是负的，减少数量其实是+1 。 如-3+1 = -2代表剩两次
                cnt = 1 + heapq.heappop(maxHeap) #从maxheap里面把他删了，并且修改剩余次数
                if cnt: #当目前此任务的次数不是0（还能继续做一次），那就把剩余次数和他下次available的时间加入q.如果是0了，上一步也在maxheap删了，就完了
                    q.append([cnt, time + n]) # 剩余count+ time it becomes available

            if q and q[0][1] == time: #q里还有东西，且q的第一个元素[-cnt, time_available] = currenttime,
                # 这就说明q中第一个task又available了（其实是最frequent的那个)。我们从q里面左边拿出来，把剩余次数加回maxheap，等着后面再次执行
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
# 我们使用tasks = ["A", "A", "A", "B", "B", "B"] 和 n = 2。

# 初始化阶段:

# count: 统计每个任务的数量。这里，我们得到：{'A': 3, 'B': 3}。
# maxHeap: 一个最大堆，初始化为任务的负数数量：[-3, -3]。
# time: 一个时间计数器，初始化为0。
# q: 一个空的双端队列。
# 开始循环:

# while maxHeap or q:：只要堆或队列中有元素，我们就继续循环。
# 第一次循环:

# time: 1
# 从maxHeap中取出一个任务，假设是A，数量从-3变为-2。
# q: 添加[-2, 3]，表示任务A的数量为2，且在时间3之前不能再执行。
# maxHeap: [-3]，只剩下任务B。
# 第二次循环:

# time: 2
# 从maxHeap中取出任务B，数量从-3变为-2。
# q: [-2, 3], [-2, 4]，现在有两个任务在队列中。
# maxHeap: 空。
# 第三次循环:

# time: 3
# maxHeap是空的，但q的第一个任务的时间戳是3，所以我们将其放回maxHeap。
# q: [-2, 4]
# maxHeap: [-2]
# 第四次循环:

# time: 4
# 从maxHeap中取出任务A，数量从-2变为-1。
# q: [-2, 4], [-1, 6]
# maxHeap: 空。
# 第五次循环:

# time: 5
# maxHeap是空的，但q的第一个任务的时间戳是6，所以我们什么都不做。
# 第六次循环:

# time: 6
# q的第一个任务的时间戳是6，所以我们将其放回maxHeap。
# q: [-1, 6]
# maxHeap: [-2]
# 第七次循环:

# time: 7
# 从maxHeap中取出任务B，数量从-2变为-1。
# q: [-1, 6], [-1, 9]
# maxHeap: 空。
# 第八次循环:

# time: 8
# maxHeap和q都是空的，所以循环结束。
# 最终，完成所有任务所需的最少时间单位是8。

# @lc code=end

