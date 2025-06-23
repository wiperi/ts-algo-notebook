#
# @lc app=leetcode.cn id=1109 lang=python3
# @lcpr version=30204
#
# [1109] 航班预订统计
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)

        for start, end, num in bookings:
            start -= 1
            end -= 1
            diff[start] += num
            diff[end + 1] -= num

        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i - 1] + diff[i]

        return res

        
# @lc code=end



#
# @lcpr case=start
# [[1,2,10],[2,3,20],[2,5,25]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,10],[2,2,15]]\n2\n
# @lcpr case=end

#

