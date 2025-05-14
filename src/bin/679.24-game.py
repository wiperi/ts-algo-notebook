#
# @lc app=leetcode.cn id=679 lang=python3
# @lcpr version=30204
#
# [679] 24 点游戏
#


# @lcpr-template-start
from itertools import combinations
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        pass

# @lc code=end

res = list(combinations([1,2,3],2))
print(res)

#
# @lcpr case=start
# [4, 1, 8, 7]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 1, 2]\n
# @lcpr case=end

#

