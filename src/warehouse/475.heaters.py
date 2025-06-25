#
# @lc app=leetcode.cn id=475 lang=python3
# @lcpr version=30204
#
# [475] 供暖器
#


# @lcpr-template-start
from bisect import bisect_left, bisect_right
from math import inf
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        maxr = 0
        for house in houses:
            r = bisect_right(heaters, house)
            l = r - 1

            ld = house - heaters[l] if l >= 0 else inf
            rd = heaters[r] - house if r < len(heaters) else inf

            minr = min(ld, rd)
            maxr = max(maxr, minr)

        return maxr


# @lc code=end


#
# @lcpr case=start
# [20]\n[1,5,8,10]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n[1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,5]\n[2]\n
# @lcpr case=end

#
