#
# @lc app=leetcode.cn id=974 lang=python3
# @lcpr version=30204
#
# [974] 和可被 K 整除的子数组
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1] 


        freq = defaultdict(int)
        freq[0] = 1
        cnt = 0
        for i in range(n):
            # print(pre[i + 1]%k, freq[pre[i + 1] % k])
            cnt += freq[pre[i + 1] % k]

            freq[pre[i + 1] % k] += 1

        return cnt
# @lc code=end



#
# @lcpr case=start
# [4,5,0,-2,-3,1]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5]\n9\n
# @lcpr case=end

#

