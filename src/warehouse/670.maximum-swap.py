#
# @lc app=leetcode.cn id=670 lang=python3
# @lcpr version=30204
#
# [670] 最大交换
#


# @lcpr-template-start
from collections import OrderedDict
from curses import beep
from math import inf
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        s = [int(n) for n in list(s)]
        arr = s

        n = len(arr)
        mx = -inf
        mi = -1
        right_max = [i for i in range(n)]

        for i in reversed(range(n)):
            if arr[i] > mx:
                mx = arr[i]
                mi = i
            right_max[i] = mi


        for i in range(n):
            if arr[i] < arr[right_max[i]]:
                arr[i], arr[right_max[i]] = arr[right_max[i]], arr[i]
                break

        return int(''.join(map(str, arr)))
# @lc code=end


#
# @lcpr case=start
# 2736\n
# @lcpr case=end

# @lcpr case=start
# 9973\n
# @lcpr case=end

#

