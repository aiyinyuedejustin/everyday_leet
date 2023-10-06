#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
# https://leetcode.cn/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (52.50%)
# Likes:    717
# Dislikes: 0
# Total Accepted:    118.1K
# Total Submissions: 225K

#
# 实现RandomizedSet 类：
# 
# 
# 
# 
# RandomizedSet() 初始化 RandomizedSet 对象
# bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
# bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
# int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 
# 
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出
# [null, true, false, true, 2, true, false, 2]
# 
# 解释
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 <= val <= 2^31 - 1
# 最多调用 insert、remove 和 getRandom 函数 2 * 10^5 次
# 在调用 getRandom 方法时，数据结构中 至少存在一个 元素。
# 
# 
# 
# 
#

# @lc code=start
class RandomizedSet:
    #https://www.youtube.com/watch?v=eKvXclLR7J8&ab_channel=CrackingFAANG

    #如果 用set， 插入，del 都是contant time， 但如果random，没法用index，得先转化为list，那样就超时了
    # 如果用dict 插入，del 都是contant time，但依然没有index
    # list -- getrandom可以，random.choice(list) -- remove最后一个确实是constant time，其他的需要shuffle是O（n）
    # insert . append 可以，但插入在其他位置不行
    #用一个list 和一个dict 

    # 如果是insert ，先append进list（永远在最后一位)， 那么在dict中，key是插入点东西，value是插入的位置(永远是最后一位 len(list) -1)
    #如果是remove， remove如果只是remove结尾的，就会O（1）.想办法让想删的在结尾： 用list和dict互换一下
    # （不是真的互换，而是拿list最后一个元素覆盖掉想删除的位置，此时list里面有两个相同的最后一个元素
    #然后把末尾删掉。 这样就相当于删了中间位置的东西
    # eg
    # item_list = [10, 20, 30, 40]
    # item_dict = {10: 0, 20: 1, 30: 2, 40: 3}
    # 我们将模拟删除值20的过程。
# 我们要删除值20。

# 检查元素是否存在:

# 首先，我们检查20是否在item_dict中。它确实在字典中，所以我们可以继续删除操作。
# 获取要删除的元素的位置和列表的最后一个元素:

# 我们获取20在item_list中的索引，即cur_idx = item_dict[20] = 1。
# 同时，我们获取item_list的最后一个元素，即last_element = 40。
# 替换要删除的元素:

# 我们将item_list中索引为cur_idx的元素替换为last_element。
# self.item_list[cur_idx] = last_element
# 现在，item_list变为：[10, 40, 30, 40]
# 更新字典中的索引:

# 我们更新item_dict中last_element的索引为cur_idx。
# item_dict[40] = cur_idx
# item_dict现在是：{10: 0, 20: 3, 30: 2, 40: 1}
# 从列表中删除最后一个元素:

# 我们从item_list中删除最后一个元素。
# item_list.pop()
# 现在，item_list变为：[10, 40, 30]
# 从字典中删除元素:

# 最后，我们从item_dict中删除20。
# del item_dict[20]
# item_dict现在是：{10: 0, 30: 2, 40: 1}
# 这样，我们成功地从item_list和item_dict中删除了20，





    def __init__(self):
        self.item_dict = {}
        self.item_list = []


    def insert(self, val: int) -> bool:
        if val not in self.item_dict: #只有不在的时候才加
            self.item_list.append(val)
        
            self.item_dict[val] = len(self.item_list) -1  #appedn的时候index永远是最后，存index方便del的时候用

            return True
        return False


    def remove(self, val: int) -> bool:
        if val not in self.item_dict:
            return False
        else:
            last_element = self.item_list[-1]
            cur_idx = self.item_dict[val]

            self.item_list[cur_idx]  = last_element
            self.item_dict[last_element] = cur_idx #交换
            self.item_list.pop()

            del self.item_dict[val]

            return True


    def getRandom(self) -> int:
        return random.choice(self.item_list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

