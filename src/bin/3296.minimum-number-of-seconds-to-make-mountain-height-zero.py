#
# @lc app=leetcode.cn id=3296 lang=python3
# @lcpr version=30204
#
# [3296] 移山所需的最少秒数
#


# @lcpr-template-start
from bisect import bisect_left
from math import floor, isqrt, sqrt
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def check(sec):
            leftHeight = mountainHeight
            for t in workerTimes:
                leftHeight -= floor((-1+sqrt(1+8*(sec/t)))/(2))
                if leftHeight <= 0:
                    return 1
            return 0
        
        lo = 0
        hi = max(workerTimes) * mountainHeight * mountainHeight

        return bisect_left(range(lo, hi + 1), 1, key=check)


# @lc code=end



#
# @lcpr case=start
# 4\n[2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3,2,2,4]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[1]\n
# @lcpr case=end

#

