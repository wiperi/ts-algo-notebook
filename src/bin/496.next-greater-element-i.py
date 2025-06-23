#
# @lc app=leetcode.cn id=496 lang=python3
# @lcpr version=30204
#
# [496] 下一个更大元素 I
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)

        larger = defaultdict(lambda: -1)
        st = []

        for i in range(n):
            while st and st[-1] < nums2[i]:
                value = st.pop()

                larger[value] = nums2[i]
            
            st.append(nums2[i])

        res = []
        for v in nums1:
            res.append(larger[v])

        return res
# @lc code=end



#
# @lcpr case=start
# [4,1,2]\n[1,3,4,2].\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n[1,2,3,4].\n
# @lcpr case=end

#

