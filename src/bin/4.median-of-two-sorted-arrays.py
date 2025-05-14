#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start
from math import ceil
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = len(nums1)
        m = len(nums2)
        
        k = 0
        if (m + n) % 2 == 1:
            k = (m + n) // 2
        else:
            k = (m + n) // 2 - 1

        a, b = 0, 0
        while k > 0:
            step = ceil(k / 2)

            if a + step <= n and b + step <= m:
                if nums1[a + step - 1] < nums2[b + step - 1]:
                    a += step
                else:
                    b += step
            elif a + step <= n:
                a += step
            elif b + step <= m:
                b += step
            else:
                break

            k -= step

        if (m + n) % 2 == 1:
            if a == n:
                return nums2[b]
            elif b == m:
                return nums1[a]
            else:
                return min(nums1[a], nums2[b])
        else:
            res = []
            i = 0
            while i < 2 and a < n:
                res.append(nums1[a])
                a += 1
                i += 1

            i = 0
            while i < 2 and b < m:
                res.append(nums2[b])
                b += 1
                i += 1

            res.sort()
            return (res[0] + res[1]) / 2
        

# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end
# @lcpr case=start
# [1,3]\n[2,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

