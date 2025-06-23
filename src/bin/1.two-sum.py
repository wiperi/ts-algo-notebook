#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30204
#
# [1] 两数之和
#


# @lcpr-template-start
from typing import List, Optional

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {v: i for i, v in enumerate(nums)}

        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in mp and mp[complement] != i:
                return [i, mp[target - nums[i]]]
            
        return None
# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#
