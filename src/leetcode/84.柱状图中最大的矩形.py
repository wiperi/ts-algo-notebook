#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30104
#
# [84] 柱状图中最大的矩形
#
from typing import List, Optional
from adt.py.leetcodeType import ListNode, TreeNode


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        # Mono Stack
        s = []

        leftBound = [0] * n
        rightBound = [0] * n

        # Get left boundary array
        for i in range(n):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()

            leftBound[i] = s[-1] if s else -1
            s.append(i)

        # Get right boundary array
        s.clear()
        for i in reversed(range(n)):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()

            rightBound[i] = s[-1] if s else n
            s.append(i)

        # Calculate area for each pillar
        for i in range(n):
            area = (rightBound[i] - leftBound[i] - 1) * heights[i]
            res = max(res, area)

        return res


class BruteForce:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        max_area = 0

        for i in range(n):
            # Calculate the maxium area

            curr_height = heights[i]

            area = heights[i]

            l = i - 1
            while l >= 0 and heights[l] >= curr_height:
                area += curr_height
                l -= 1

            r = i + 1
            while r < n and heights[r] >= curr_height:
                area += curr_height
                r += 1

            max_area = max(max_area, area)
            # print('i', i, 'area', area)

        return max_area


# @lc code=end


#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#
