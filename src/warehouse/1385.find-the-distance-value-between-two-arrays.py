#
# @lc app=leetcode.cn id=1385 lang=python3
# @lcpr version=30204
#
# [1385] 两个数组间的距离值
#


# @lcpr-template-start
from bisect import bisect_right
from math import inf
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        arr2 = [-inf] + arr2 + [inf]
        cnt = 0

        for val in arr1:
            r = bisect_right(arr2, val)
            l = r - 1
            if val - arr2[l] > d and arr2[r] - val > d:
                cnt += 1

        return cnt


# @lc code=end


#
# @lcpr case=start
# [4,5,8]\n[10,9,1,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,3]\n[-4,-3,6,10,20,30]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1,100,3]\n[-5,-2,10,-3,7]\n6\n
# @lcpr case=end

#
