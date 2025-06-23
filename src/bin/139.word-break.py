#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#


# @lcpr-template-start
from functools import cache
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(i: int):
            if s[i:] == '':
                return True
            for w in wordDict:
                if s[i:].startswith(w):
                    if dfs(len(w)):
                        return True
                    else:
                        pass
            return False

        return dfs(s)
# @lc code=end

#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

