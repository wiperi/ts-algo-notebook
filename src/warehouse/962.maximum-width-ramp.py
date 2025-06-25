#
# @lc app=leetcode.cn id=962 lang=python3
# @lcpr version=30204
#
# [962] 最大宽度坡
#


# @lcpr-template-start
from math import inf
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution(object):
    def maxWidthRamp(self, A):
        max_gap = 0
        leftmost = inf
        for i in sorted(range(len(A)), key = A.__getitem__):
            max_gap = max(max_gap, i - leftmost)
            leftmost = min(leftmost, i)
        return max_gap
        
# @lc code=end



#
# @lcpr case=start
# [6,0,8,2,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [9,8,1,0,1,9,4,0,4,1]\n
# @lcpr case=end

#

