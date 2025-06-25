#
# @lc app=leetcode.cn id=1094 lang=python3
# @lcpr version=30204
#
# [1094] 拼车
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trips, key=lambda a: a[2])[2] + 1

        diff = [0] * n
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num

        arr = [0] * n
        arr[0] = diff[0]
        for i in range(1, n):
            arr[i] = arr[i - 1] + diff[i]

        return max(arr) <= capacity


# @lc code=end


#
# @lcpr case=start
# [[2,1,5],[3,3,7]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,5],[3,3,7]]\n5\n
# @lcpr case=end

#
