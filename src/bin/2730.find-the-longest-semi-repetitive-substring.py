#
# @lc app=leetcode.cn id=2730 lang=python3
# @lcpr version=30204
#
# [2730] 找到最长的半重复子字符串
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = r = 0
        pair = 0
        mlen = 0
        while r < len(s):
            added = s[r]
            if r > 0 and added == s[r - 1]:
                pair += 1
            r += 1

            if pair > 1:
                while l < r and s[l] != s[l + 1]:
                    l += 1
                l += 1
                pair -= 1
            
            mlen = max(mlen, r - l)

        return mlen
# @lc code=end



#
# @lcpr case=start
# "52233"\n
# @lcpr case=end

# @lcpr case=start
# "5494"\n
# @lcpr case=end

# @lcpr case=start
# "1111111"\n
# @lcpr case=end

#

