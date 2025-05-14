#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start
from typing import Counter, List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(s)
        m = len(p)

        if n < m:
            return []

        win = [0] * 26

        def ind(ch: str):
            return ord(ch) - ord("a")

        for i in range(m):
            win[ind(s[i])] += 1
            win[ind(p[i])] -= 1

        diff = [c != 0 for c in win].count(True)

        res = []
        if diff == 0:
            res.append(0)

        l, r = 0, m

        while r < n:
            if win[ind(s[r])] == -1:
                diff -= 1
            elif win[ind(s[r])] == 0:
                diff += 1

            win[ind(s[r])] += 1

            if win[ind(s[l])] == 1:
                diff -= 1
            elif win[ind(s[l])] == 0:
                diff += 1

            win[ind(s[l])] -= 1

            if diff == 0:
                res.append(l + 1)

            r += 1
            l += 1

        return res


# @lc code=end


#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#
