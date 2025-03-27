#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = int(10 ** 5)

        maxProfit = 0

        for p in prices:
            minPrice = min(minPrice, p)

            maxProfit = max(maxProfit, p - minPrice)

        return maxProfit
            

        
# @lc code=end

    