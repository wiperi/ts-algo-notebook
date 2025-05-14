#
# @lc app=leetcode.cn id=503 lang=python3
# @lcpr version=30204
#
# [503] 下一个更大元素 II
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        larger = [-1] * n
        st = [] # index

        for i in range(n * 2):
            i = i % n
            
            while st and nums[st[-1]] < nums[i]:
                prevInd = st.pop()

                larger[prevInd] = nums[i]
            
            st.append(i)

        
        return larger
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,3]\n
# @lcpr case=end

#

