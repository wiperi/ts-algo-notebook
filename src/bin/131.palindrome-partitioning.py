#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        parts = []
        res = []
        def backtrack(start):

            if start == n:
                res.append(parts.copy())

            for i in range(start, n):
                substr = s[start: i + 1]
                if substr == substr[::-1]:
                    parts.append(substr)
                    backtrack(i + 1)
                    parts.pop()

        backtrack(0)
        return res
                


# @lc code=end

Solution().partition("aab")
#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#
