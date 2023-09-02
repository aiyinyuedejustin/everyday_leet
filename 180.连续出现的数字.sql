--
-- @lc app=leetcode.cn id=180 lang=mysql
--
-- [180] 连续出现的数字
--
-- https://leetcode.cn/problems/consecutive-numbers/description/
--
-- database
-- Medium (47.60%)
-- Likes:    790
-- Dislikes: 0
-- Total Accepted:    159.7K
-- Total Submissions: 335.5K
-- Testcase Example:  '{"headers": {"Logs": ["id", "num"]}, "rows": {"Logs": [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}'
--
-- 表：Logs
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- 在 SQL 中，id 是该表的主键。
-- id 是一个自增列。
-- 
-- 
-- 
-- 找出所有至少连续出现三次的数字。
-- 
-- 返回的结果表中的数据可以按 任意顺序 排列。
-- 
-- 结果格式如下面的例子所示：
-- 
-- 
-- 
-- 示例 1:
-- 
-- 
-- 输入：
-- Logs 表：
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- 输出：
-- Result 表：
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- 解释：1 是唯一连续出现至少三次的数字。
-- 
--

-- @lc code=start
# Write your MySQL query statement below


select distinct a.num as ConsecutiveNums
from logs a , logs b, logs c
where a.id = b.id-1 and b.id= c.id -1 and a.num=b.num and b.num = c.num
-- @lc code=end


