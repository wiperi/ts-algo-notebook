#
# @lc app=leetcode.cn id=904 lang=python3
# @lcpr version=30204
#
# [904] 水果成篮
#


# @lcpr-template-start
from collections import defaultdict
from distutils.command.build_scripts import first_line_re
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        win = defaultdict(int)
        l, r = 0, 0
        mlen = 0
        while r < len(fruits):
            win[fruits[r]] += 1
            r += 1

            while len(win) > 2:
                win[fruits[l]] -= 1
                if win[fruits[l]] == 0:
                    del win[fruits[l]]
                l += 1
                

            mlen = max(mlen, r - l)

        return mlen
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,4,1,4,1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,1,2,1,1,2,3,3,4]\n
# @lcpr case=end

#

