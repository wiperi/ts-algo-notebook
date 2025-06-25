#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])

        n = len(intervals)

        res = []

        i = 0
        while i < n:
            j = i + 1
            while j < n and intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j += 1

            res.append([intervals[i][0], intervals[i][1]])

            i = j

        return res


# @lc code=end


#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#
