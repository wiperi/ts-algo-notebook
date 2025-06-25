#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        leftParen = {'(', '[','{'}
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in leftParen:
                st.append(ch)
            else:
                if not st or st.pop() != mp[ch]:
                    return False
        
        return len(st) == 0
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#

