#
# @lc app=leetcode.cn id=2070 lang=python3
# @lcpr version=30204
#
# [2070] 每一个查询的最大美丽值
#


# @lcpr-template-start
from bisect import bisect_left, bisect_right
from itertools import permutations
from re import L
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[1])
        items.sort()

        newItems = []
        n = len(items)
        i = 0
        while i < n:
            i = bisect_right(items, items[i][0], key=lambda a : a[0])
            newItems.append(items[i - 1])

        items = newItems

        premax = []
        lm = 0
        for it in items:
            lm = max(lm, it[1])
            premax.append(lm)

        # print(newItems)

        res = []

        for price in queries:
            r = bisect_right(items, price, key=lambda a: a[0])
            if r == 0:
                res.append(0)
                continue

            maxBeauty = premax[r - 1]

            res.append(maxBeauty)

        return res


# @lc code=end


#
# @lcpr case=start
# [[1,2],[3,2],[2,4],[5,6],[3,5]]\n[1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,2],[1,3],[1,4]]\n[1]\n
# @lcpr case=end

# @lcpr case=start
# [[10,1000]]\n[5]\n
# @lcpr case=end

#
