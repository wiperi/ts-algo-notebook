#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30204
#
# [118] 杨辉三角
#


# @lcpr-template-start
from bisect import bisect_left
from itertools import groupby, pairwise
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def f(x):
            if x == 1:
                return [1]
            if x == 2:
                return [1,1]

            res = [1]
            for a, b in pairwise(f(x - 1)):
                res.append(a + b)
            res += [1]

            return res
        
        return f(numRows)
        
# @lc code=end

def problem(a):
    def check(x) -> bool:
        pass

    lo, hi = None, None

    return bisect_left([check(x) for x in range(lo, hi + 1)], True)
#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

