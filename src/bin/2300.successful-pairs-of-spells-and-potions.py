#
# @lc app=leetcode.cn id=2300 lang=python3
# @lcpr version=30204
#
# [2300] 咒语和药水的成功对数
#


# @lcpr-template-start
from bisect import bisect_left, bisect_right
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        def findleft(target):
            l, r = 0, n -1

            while l <= r:
                mid = (l + r) // 2
                midv = potions[mid]

                if target == midv:
                    r = mid - 1
                elif target > midv:
                    l = mid + 1
                elif target < midv:
                    r = mid - 1

            return l

        res = []
        for sp in spells:
            left = findleft(success / sp)
            res.append(len(potions) - left)

        return res


# @lc code=end

#
# @lcpr case=start
# [5,1,3]\n[1,2,3,4,5]\n7\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n[8,5,8]\n16\n
# @lcpr case=end

#
