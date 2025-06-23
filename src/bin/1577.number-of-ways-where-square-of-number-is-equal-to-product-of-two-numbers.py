#
# @lc app=leetcode.cn id=1577 lang=python3
# @lcpr version=30204
#
# [1577] 数的平方等于两数乘积的方法数
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        nums1.sort()
        nums2.sort()

        def f(a, b):
            cnt = 0
            n = len(b)
            for t in a:
                t = t**2
                l, r = 0, n - 1

                while l < r:
                    p = b[l] * b[r]

                    if p == t and b[l] == b[r]:
                        length = r - l + 1
                        cnt += length * (length - 1) // 2
                        break
                    elif p == t:
                        len_left = 1
                        len_right = 1

                        l += 1
                        while l < r and b[l] == b[l - 1]: 
                            len_left += 1
                            l += 1

                        r -= 1
                        while l < r and b[r] == b[r + 1]:
                            len_right += 1
                            r -= 1
                        
                        cnt += len_left * len_right
                    elif p < t:
                        l += 1
                    else:
                        r -= 1
            return cnt
                

        return f(nums1, nums2) + f(nums2, nums1)
# @lc code=end



#
# @lcpr case=start
# [7,4]\n[5,2,8,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n[1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,8,3]\n[1,2,9,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,7,9,11,23]\n[3,5,1024,12,18]\n
# @lcpr case=end

#

