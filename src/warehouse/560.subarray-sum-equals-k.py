#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start
from collections import defaultdict
from itertools import accumulate
from typing import List, Optional


# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pre = list(accumulate(nums))
        pre.insert(0, 0)

        mp = defaultdict(int)
        mp[0] = 1
        cnt = 0
        for i in range(1, n + 1):
            cnt += mp[pre[i] - k]
            mp[pre[i]] += 1

        return cnt


# @lc code=end

res = Solution().subarraySum([1, -1, 0], 0)
print(res)
#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#
