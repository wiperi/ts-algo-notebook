#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30104
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(s)

        pc = Counter(p)
        sc = Counter(s[: len(p)])

        if pc == sc:
            res.append(0)

        for l, r in zip(range(0, n - len(p)), range(len(p), n)):
            # Remove left
            sc[s[l]] -= 1
            if sc[s[l]] == 0:
                del sc[s[l]]

            # Add right
            sc[s[r]] = sc.get(s[r], 0) + 1

            # Check validity
            if pc == sc:
                res.append(l + 1)

        return res

    def __init__(self) -> None:
        pass


# @lc code=end


#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#
