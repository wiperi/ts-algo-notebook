#
# @lc app=leetcode.cn id=63 lang=python3
# @lcpr version=30204
#
# [63] 不同路径 II
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def f(r, c):
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
                return 0
            return f(r - 1, c) + f(r, c - 1)

        return f(m - 1, n - 1)
# @lc code=end



#
# @lcpr case=start
# [[0,0,0],[0,1,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

#

