#
# @lc app=leetcode.cn id=1094 lang=python3
# @lcpr version=30204
#
# [1094] 拼车
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        merge interval
        '''

        trips.sort(key=lambda a:a[1])

        i = 0
        n = len(trips)

        while i < n:

            lmax = trips[i][0]

            j = i + 1
            while j < n and trips[j][1] < trips[i][2]:
                lmax += trips[j][0]
                j += 1

            if lmax > capacity:
                return False
            
            i += 1
            
        return True
# @lc code=end



#
# @lcpr case=start
# [[2,1,5],[3,3,7]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,5],[3,3,7]]\n5\n
# @lcpr case=end

#

