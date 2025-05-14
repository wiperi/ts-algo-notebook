#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30204
#
# [84] 柱状图中最大的矩形
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        for pillar at index i

        let right be the index of first smaller value
        same for left     

        max area = (right - left) * height[i]
        '''

        n = len(heights)
        
        leftBound = [-1] * n
        st = []
        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                st.pop()

            if st:
                leftBound[i] = st[-1]
            
            st.append(i)

        rightBound = [n] * n
        st = []
        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                rightBound[st.pop()] = i
            
            st.append(i)

        area = [0] * n
        for i in range(n):
            area[i] = (rightBound[i] - leftBound[i] - 1) * heights[i]

        return max(area)


# @lc code=end



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#

