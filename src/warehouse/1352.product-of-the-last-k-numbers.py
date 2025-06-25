#
# @lc app=leetcode.cn id=1352 lang=python3
# @lcpr version=30204
#
# [1352] 最后 K 个数的乘积
#


# @lcpr-template-start
from audioop import reverse
from bisect import bisect, bisect_left
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pre = [1]
            return

        self.pre.append(self.pre[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.pre) - 1:
            return 0

        return int(self.pre[-1] / self.pre[-k - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end
#
# @lcpr case=start
# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"][[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]\n
# @lcpr case=end

#
