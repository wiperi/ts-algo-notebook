#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#


# @lcpr-template-start
from heapq import heappop as heappop, heappush as heappush, heappushpop
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class MedianFinder:

    def __init__(self):
        self.maxpq = []
        self.minpq = []

    def balance(self):
        minN = len(self.minpq)
        maxN = len(self.maxpq)

        if maxN - minN > 1:
            heappush(self.minpq, -heappop(self.maxpq))
        elif minN - maxN > 1:
            heappush(self.maxpq, -heappop(self.minpq))

    def addNum(self, num: int) -> None:
        if not self.maxpq or num < self.maxpq[0]:
            heappush(self.maxpq, -num)
        else:
            heappush(self.minpq, num)

        self.balance()

    def findMedian(self) -> float:
        minN = len(self.minpq)
        maxN = len(self.maxpq)

        if (minN + maxN) % 2 == 0:
            return (self.minpq[0] + -self.maxpq[0]) / 2
        else:
            return -self.maxpq[0] if maxN > minN else self.minpq[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
