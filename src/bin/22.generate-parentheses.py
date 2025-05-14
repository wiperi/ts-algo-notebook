#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        length = n * 2

        path = []
        res = []
        balance = 0
        def backtrack():
            nonlocal balance

            if len(path) == length:
                if balance == 0:    
                    res.append(''.join(path))
                return

            for p in ['(', ')']:
                if p == ')' and balance < 1:
                    continue

                if p == '(':
                    balance += 1
                else:
                    balance -= 1
                path.append(p)
                backtrack()
                path.pop()
                if p == '(':
                    balance -= 1
                else:
                    balance += 1
        
        backtrack()

        return res


# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

