#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List

# @lc code=start

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp(i, j) = min path sum from start to (i, j)
        # dp(i, j) = min(dp(i - 1, j), dp(i, j - 1))

        m = len(grid)
        n = len(grid[0])

        dp = grid
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j]
                else : dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]

        return dp[-1][-1]

# @lc code=end
