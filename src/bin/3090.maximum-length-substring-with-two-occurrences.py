#
# @lc app=leetcode.cn id=3090 lang=python3
# @lcpr version=30204
#
# [3090] 每个字符最多出现两次的最长子字符串
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # shrink when any char freq > 2
        l, r = 0, 0
        ind = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        win = [0] * 26
        mlen = 0
        while r < len(s):
            add = ind[s[r]]
            win[add] += 1
            r += 1

            while win[add] > 2:
                remove = ind[s[l]]
                win[remove] -= 1
                l += 1

            mlen = max(mlen, r - l)

        return mlen
# @lc code=end


#
# @lcpr case=start
# "bcbbbcba"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

#

