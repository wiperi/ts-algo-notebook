#
# @lc app=leetcode.cn id=3325 lang=python3
# @lcpr version=30204
#
# [3325] 字符至少出现 K 次的子字符串 I
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        # if [i..j] is valid then [0..j] has to be valid
        win = [0] * 26
        ind = {chr(ord("a") + i): i for i in range(26)}

        l = r = cnt = 0
        while r < len(s):
            win[ind[s[r]]] += 1
            r += 1

            while l < r and win[ind[s[r - 1]]] >= k:
                win[ind[s[l]]] -= 1
                l += 1

            cnt += l
        return cnt


# @lc code=end


#
# @lcpr case=start
# "abacb"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n1\n
# @lcpr case=end

#
