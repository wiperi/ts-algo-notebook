#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start
from typing import Counter, List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0

        def hasDup(s):
            used = set()
            for ch in s:
                if ch in used:
                    return True
                used.add(ch)
            return False
        
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if not hasDup(sub):
                    maxlen = max(maxlen , len(sub))

        return maxlen



                
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

