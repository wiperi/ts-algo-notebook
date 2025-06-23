#
# @lc app=leetcode.cn id=598 lang=python3
# @lcpr version=30204
#
# [598] 区间加法 II
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        diff = [[0] * n for _ in range(m)]

        for x, y in ops:
            diff[x][y] += 1

        
# @lc code=end



#
# @lcpr case=start
# 3\n[[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[]\n
# @lcpr case=end

#

