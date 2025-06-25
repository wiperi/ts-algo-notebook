#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start
from math import ceil, inf
from typing import List, Optional

from numpy import append
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
        
        nums1.extend([inf for _ in range(2)])
        nums2.extend([inf for _ in range(2)])
        if (m + n) % 2 == 1:
            return min(nums1[a], nums2[b])
        else:
            res = []
            for _ in range(2):
                res.append(nums1[a])
                res.append(nums2[b])
                a += 1
                b += 1
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

