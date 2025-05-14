#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target = set(t)

        win = defaultdict(int)
        for c in t:
            win[c] -= 1
        diff = len(win)

        n = len(s)

        minLen = 10**10
        res = ""
        l, r = 0, 0
        while r < n:
            ch = s[r]
            if ch in target and win[ch] == -1:
                diff -= 1
            win[ch] += 1
            r += 1

            foundOne = False
            while l <= r and diff == 0:
                foundOne = True
                ch = s[l]
                if ch in target and win[ch] == 0:
                    diff += 1
                win[ch] -= 1
                l += 1

            if l <= r and foundOne:
                # print(s[l - 1:r], win, diff)
                localLen = r - l + 1
                if localLen < minLen:
                    minLen = localLen
                    res = s[l - 1:r]


        return res


# @lc code=end


#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#
