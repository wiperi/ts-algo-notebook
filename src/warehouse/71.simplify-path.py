#
# @lc app=leetcode.cn id=71 lang=python3
# @lcpr version=30204
#
# [71] 简化路径
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        go back
        '''

        st = []

        path = path.split('/')
        for token in path:
            if token == '' or token == '.':
                continue
            elif token == '..':
                if st: st.pop()
            else:
                st.append(token)

        return '/' + '/'.join(st)
        
# @lc code=end



#
# @lcpr case=start
# "/home/"\n
# @lcpr case=end

# @lcpr case=start
# "/home//foo/"\n
# @lcpr case=end

# @lcpr case=start
# "/home/user/Documents/../Pictures"\n
# @lcpr case=end

# @lcpr case=start
# "/../"\n
# @lcpr case=end

# @lcpr case=start
# "/.../a/../b/c/../d/./"\n
# @lcpr case=end

#

