#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30204
#
# [155] 最小栈
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class MinStack:

    def __init__(self):
        self.diff = []
        self.minval = 0

    def push(self, val: int) -> None:
        if not self.diff:
            self.diff.append(0)
            self.minval = val
        else:
            diff = val - self.minval
            self.diff.append(diff)
            if diff < 0:
                self.minval = val

    def pop(self) -> None:
        diff = self.diff.pop()
        if diff < 0:
            self.minval = self.minval - diff

    def top(self) -> int:
        if self.diff[-1] < 0:
            return self.minval
        else:
            return self.diff[-1] + self.minval

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

