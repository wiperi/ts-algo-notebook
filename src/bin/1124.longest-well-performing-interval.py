#
# @lc app=leetcode.cn id=1124 lang=python3
# @lcpr version=30204
#
# [1124] 表现良好的最长时间段
#


# @lcpr-template-start
from bisect import bisect_left, bisect_right
import bisect
from traceback import print_tb
from typing import List, Optional


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestWPI(self, arr: List[int]) -> int:
        """
        if arr[i] > 8, then it be 1 (tiring day)
        else it'd be -1 (non-tiring day)

        find a sub arr, that its sum > 0, and it is longest
        """
        n = len(arr)
        arr = [1 if v > 8 else -1 for v in arr]

        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + arr[i - 1]

        # Store indices of prefix sums
        st = []
        for i in range(n + 1):
            # if not st or presum[i] < presum[st[-1]]:
            st.append(i)
        
        mlen = 0
        # Iterate from right to left to find the longest interval
        for j in range(n, 0, -1):
            while st and presum[j] > presum[st[-1]]:
                mlen = max(mlen, j - st[-1])
                st.pop()
        
        return mlen


Solution().longestWPI([8,10,6,16,5])


# @lc code=end


#
# @lcpr case=start
# [9,9,6,0,6,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,6]\n
# @lcpr case=end

#
