#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start
from curses.ascii import isdigit
import re
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        n = len(s)
        i = 0

        def getNumber():
            nonlocal i
            start = i
            i += 1
            while i < n and s[i].isdigit():
                i += 1
            return int(s[start: i])


        while i < n:
            if s[i].isdigit():
                repeat = getNumber()
                st.append(repeat)
            elif s[i].isalpha() or s[i] == '[':
                st.append(s[i])
                i += 1
            elif s[i] == ']':
                substr = ''
                while st[-1] != '[':
                    substr = st.pop() + substr
                st.pop()
                repeat = st.pop()
                st.append(repeat * substr)
                i += 1

        # Combine all strings in the stack
        result = ''
        for item in st:
            result += item
        
        return result
            


# Test case
# print(Solution().decodeString("3[a]2[bc]"))


# @lc code=end


#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#
