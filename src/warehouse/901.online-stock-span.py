#
# @lc app=leetcode.cn id=901 lang=python3
# @lcpr version=30204
#
# [901] 股票价格跨度
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class StockSpanner:

    def __init__(self):
        self.price = []
        self.st = []

    # find first large on left
    def next(self, price: int) -> int:
        self.price.append(price)
        n = len(self.price)

        while self.st and self.price[self.st[-1]] <= price:
            self.st.pop()

        if self.st:
            res = n - 1 - self.st[-1]
        else:
            res = n - 1 - (-1)
        self.st.append(n - 1)

        # print([self.price[i] for i in self.st])

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end


#
# @lcpr case=start
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"][[], [100], [80], [60], [70], [60], [75], [85]]\n
# @lcpr case=end

#
