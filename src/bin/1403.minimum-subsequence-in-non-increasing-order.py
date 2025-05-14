#
# @lc app=leetcode.cn id=1403 lang=python3
# @lcpr version=30204
#
# [1403] 非递增顺序的最小子序列
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort(reverse=True)

        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]

        for i in range(n):
            lsum = presum[i + 1]
            rsum = presum[n] - presum[i + 1]

            if lsum > rsum:
                return sorted(nums[:i + 1], reverse=True)

        raise Exception()



        
# @lc code=end



#
# @lcpr case=start
# [4,3,10,9,8]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,7,6,7]\n
# @lcpr case=end

#

