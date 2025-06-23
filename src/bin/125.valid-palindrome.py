#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30204
#
# [125] 验证回文串
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join([ch.lower() for ch in s if ch.isalpha() or s.isdigit()])
        print(ss)
        return ss == ss[::-1]
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

