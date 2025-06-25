#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start
from typing import Counter, List, Optional
# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()

        l = r = 0
        mlen = 0
        while r < len(s):
            add = s[r]
            while add in win:
                win.discard(s[l])
                l += 1

            win.add(add)
            r += 1

            mlen = max(mlen, r - l)

        return mlen



                
Solution().lengthOfLongestSubstring('aa')

# @lc code=end



#
# @lcpr case=start
# "aabaab!bb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

