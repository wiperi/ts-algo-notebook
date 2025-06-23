#
# @lc app=leetcode.cn id=1471 lang=python3
# @lcpr version=30204
#
# [1471] 数组中的 k 个最强值
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        mid = (len(arr) - 1) // 2

        dist_arr = [(abs(v - arr[mid]), v) for i, v in enumerate(arr)]
        dist_arr.sort(reverse=True)
        return [n[1] for n in dist_arr[:k]]
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,5,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [6,7,11,7,6,8]\n5\n
# @lcpr case=end

#

