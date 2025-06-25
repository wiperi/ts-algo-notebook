#
# @lc app=leetcode.cn id=1208 lang=python3
# @lcpr version=30204
#
# [1208] 尽可能使字符串相等
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l, r = 0, 0 
        cost = 0
        mlen = 0
        while r < len(s):
            add = abs(ord(s[r]) - ord(t[r]))
            cost += add
            r += 1

            while l < len(s) and cost > maxCost:
                remove = abs(ord(s[l]) - ord(t[l]))
                cost -= remove
                l += 1

            mlen = max(mlen, r - l)

        return mlen
# @lc code=end



#
# @lcpr case=start
# "abcd"\n"bcdf"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"cdef"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"acde"\n0\n
# @lcpr case=end

#

