#
# @lc app=leetcode.cn id=1248 lang=python3
# @lcpr version=30204
#
# [1248] 统计「优美子数组」
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if v % 2 == 1 else 0 for v in nums]
        def fn(arr: list, goal):
            l = r = s = cnt = 0
            while r < len(arr):
                s += arr[r]
                r += 1

                while l < r and s >= goal:
                    s -= arr[l]
                    l += 1
                cnt += l
            return cnt
        
        return fn(nums, k) - fn(nums, k + 1)
# @lc code=end



#
# @lcpr case=start
# [1,1,2,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,1,2,2,1,2,2,2]\n2\n
# @lcpr case=end

#

