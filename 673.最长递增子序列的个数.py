#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
from typing import List
# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp(i) = of nums[0..i], len of longest LIS
        # cnt(i) = of nums[0..i], num of longest LIS

        n = len(nums)
        dp = [1] * n
        cnt = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        # Find a longer LIS in nums[0..i]
                        dp[i] = dp[j] + 1
                        # Reset counter
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        # Find a another case of longest LIS
                        cnt[i] += cnt[j]
                    else:
                        # Find a case of LIS but it is not the longest
                        continue

        
        maxLisLen = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == maxLisLen:
                res += cnt[i]

        return res
# @lc code=end

