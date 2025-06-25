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


# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        p = 0

        st = []

        def getDigit(i):
            number = ''
            while s[i].isdigit():
                number += s[i]
                i += 1
            nonlocal p
            p = i
            return int(number)
        
        while p < n:
            if s[p].isdigit():
                repeat = getDigit(p)
                st.append(repeat)
                st.append(s[p])
            elif s[p].isalpha():
                st.append(s[p])
            elif s[p] == ']':
                part = ''
                while st and st[-1] != '[':
                    part = st.pop() + part
                st.pop()
                repeat = st.pop()
                part = repeat * part
                st.append(part)

            p += 1

        return ''.join(st)



# Test case
# print(Solution().decodeString("3[a]2[bc]"))


# @lc code=end
print(213 is int)

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
