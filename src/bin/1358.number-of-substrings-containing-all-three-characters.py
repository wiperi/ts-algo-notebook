#
# @lc app=leetcode.cn id=1358 lang=python3
# @lcpr version=30204
#
# [1358] 包含所有三种字符的子字符串数目
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = r = 0
        win = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        res = 0

        while r < len(s):
            add = s[r]
            if add == 'a' or add == 'b' or add == 'c':
                win[add] += 1
            r += 1

            while all(win[i] > 0 for i in ['a','b','c']):
                remove = s[l]
                if remove == 'a' or remove == 'b' or remove == 'c':
                    win[remove] -= 1
                l += 1
            res += l

        return res
# @lc code=end



#
# @lcpr case=start
# "abcabc"\n
# @lcpr case=end

# @lcpr case=start
# "aaacb"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

