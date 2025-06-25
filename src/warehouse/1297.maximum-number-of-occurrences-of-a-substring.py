#
# @lc app=leetcode.cn id=1297 lang=python3
# @lcpr version=30204
#
# [1297] 子串的最大出现次数
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        appear = defaultdict(int)
        n = len(s)

        size = minSize
        win = defaultdict(int)
        for i in range(size):
            win[s[i]] += 1

        if len(win) <= maxLetters:
            appear[s[:size]] += 1

        l, r = 0, size
        while r < n:
            win[s[r]] += 1
            win[s[l]] -= 1
            if win[s[l]] == 0:
                del win[s[l]]

            if len(win) <= maxLetters:
                appear[s[l + 1 : r + 1]] += 1

            r += 1
            l += 1

        return max(appear.values()) if len(appear) else 0


# @lc code=end


#
# @lcpr case=start
# "aababcaab"\n2\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n1\n3\n3\n
# @lcpr case=end

# @lcpr case=start
# "aabcabcab"\n2\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n2\n3\n3\n
# @lcpr case=end

#
