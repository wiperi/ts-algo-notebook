#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start
import bisect
from itertools import accumulate
from math import inf
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 思考，对于位置i，若a[i..j] 和 = target，那么j之后的所有位置都可以跳过

        presum = [0] + list(accumulate(nums))
        res = inf
        for i in range(1, len(presum)):
            t = presum[i] - target
            ind = bisect.bisect_right(presum, t, 0, i) - 1
            if ind >= 0:
                res = min(res, i - ind)

        return res if res != inf else 0


# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

