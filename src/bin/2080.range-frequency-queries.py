#
# @lc app=leetcode.cn id=2080 lang=python3
# @lcpr version=30204
#
# [2080] 区间内查询数字的频率
#


# @lcpr-template-start
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        # [[1,1],[3,2],[index, freq]]
        self.mp = defaultdict(lambda: [(0, 0)])
        for i, v in enumerate(arr):
            i += 1
            ls = self.mp[v]
            ls.append((i, ls[-1][1] + 1))

    def query(self, left: int, right: int, value: int) -> int:
        ls = self.mp[value]

        l = bisect_right(ls, left, key=lambda a: a[0]) - 1
        r = bisect_right(ls, right + 1, key=lambda a: a[0]) - 1

        # print(ls, l, r)

        return ls[r][1] - ls[l][1]


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end

q = RangeFreqQuery([1, 1, 1, 2, 2])
print(q.query(0, 1, 2))


#
# @lcpr case=start
# ["RangeFreqQuery", "query", "query"][[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]\n
# @lcpr case=end

#
