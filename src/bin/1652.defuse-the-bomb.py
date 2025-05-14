#
# @lc app=leetcode.cn id=1652 lang=python3
# @lcpr version=30204
#
# [1652] 拆炸弹
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        '''
        we create a window of length k
        window move n times
        if k > 0, then the sum of window is assign to its left val
        if k < 0, it is right val
        '''
        n = len(code)
        res = [0] * n
        
        window = 0
        for i in range(abs(k)):
            window += code[i]
        if k > 0:
            res[-1 % n] = window
        else:
            res[k % n] = window

        l, r = 0, (abs(k)) - 1

        for _ in range(n):
            r = (r + 1) % n
            window += code[r]

            window -= code[l]
            l = (l + 1) % n

            if k > 0:
                res[(l - 1) % n] = window
            else:
                res[(r + 1) % n] = window

        return res
# @lc code=end

#
# @lcpr case=start
# [5,7,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,4,9,3]\n-2\n
# @lcpr case=end

#

