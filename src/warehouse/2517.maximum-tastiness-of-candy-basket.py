#
# @lc app=leetcode.cn id=2517 lang=python3
# @lcpr version=30204
#
# [2517] 礼盒的最大甜蜜度
#


# @lcpr-template-start
import itertools
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort(reverse=True)

        return abs(price[0] - price[-k + 1])
# @lc code=end



#
# @lcpr case=start
# [13,5,1,8,21,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7]\n2\n
# @lcpr case=end

#

