#
# @lc app=leetcode.cn id=1750 lang=python3
# @lcpr version=30204
#
# [1750] 删除字符串两端相同字符后的最短长度
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        l, r = 0, n - 1

        while l < r and s[l] == s[r]:

            l += 1
            while l < r and s[l] == s[l - 1]:
                l += 1

            r -= 1
            while l < r and s[r] == s[r + 1]:
                r -= 1

        return r - l + 1

# @lc code=end



#
# @lcpr c
# ase=start
# "ca"\n
# @lcpr case=end

# @lcpr case=start
# "cabaabac"\n
# @lcpr case=end

# @lcpr case=start
# "aabccabba"\n
# @lcpr case=end

#

