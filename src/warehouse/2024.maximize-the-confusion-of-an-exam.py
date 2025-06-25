#
# @lc app=leetcode.cn id=2024 lang=python3
# @lcpr version=30204
#
# [2024] 考试的最大困扰度
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        # you may change at most k values
        # a array with 1 and 0 like [1,1,1,1,0,0,1,1,1]
        # what is the longest sequence of 1 or 0
        mlen = 0
        l = r = 0
        modify = 0
        # longest T seq
        while r < len(s):
            if s[r] == 'F':
                modify += 1
            r += 1

            if modify > k:
                while l < len(s) and s[l] != 'F':
                    l += 1
                l += 1
                modify -= 1

            mlen = max(mlen, r - l)

        l = r = 0
        modify = 0
        # longest F seq
        while r < len(s):
            if s[r] == 'T':
                modify += 1
            r += 1

            if modify > k:
                while l < len(s) and s[l] != 'T':
                    l += 1
                l += 1
                modify -= 1

            mlen = max(mlen, r - l)

        return mlen



# @lc code=end



#
# @lcpr case=start
# "TTFF"\n2\n
# @lcpr case=end

# @lcpr case=start
# "TFFT"\n1\n
# @lcpr case=end

# @lcpr case=start
# "TTFTTFTT"\n1\n
# @lcpr case=end

#

