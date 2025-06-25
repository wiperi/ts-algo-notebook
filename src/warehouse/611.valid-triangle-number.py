#
# @lc app=leetcode.cn id=611 lang=python3
# @lcpr version=30204
#
# [611] 有效三角形的个数
#


# @lcpr-template-start
from itertools import groupby
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        pass
# @lc code=end

a = [1,1,1,2,2]
for v, g in groupby(a):
    print(v)
    print(len(list(g)))

#
# @lcpr case=start
# [2,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,3,4]\n
# @lcpr case=end

#

