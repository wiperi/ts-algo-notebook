#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        path = []
        res = []
        n = len(digits)

        def backtrack(ind):

            if ind == n:
                res.append(''.join(path))
                return

            for c in mp[digits[ind]]:
                path.append(c)
                backtrack(ind + 1)
                path.pop()

        backtrack(0)

        return res


# @lc code=end


#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#
