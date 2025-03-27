#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30104
#
# [238] 除自身以外数组的乘积
#
from typing import List

# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Prefix Sum

        # Build 2 array.
        # One is accumulative product from left to right
        # One is that of from right to left

        # Then, the res[i] = product_left[i - 1] * product_right[i + 1]

        n = len(nums)
        pleft = [0] * n
        pright = [0] * n

        p = 1
        for i in range(n):
            p = p * nums[i]
            pleft[i] = p

        p = 1
        for i in reversed(range(n)):
            p = p * nums[i]
            pright[i] = p

        res = [0] * n
        for i in range(n):
            if i == 0:
                res[i] = pright[i + 1]
            elif i == n - 1:
                res[i] = pleft[i - 1]
            else:
                res[i] = pleft[i - 1] * pright[i + 1]

        return res


def MoreConcise():
    class Solution:
        def productExceptSelf(self, nums: list[int]) -> list[int]:
            n = len(nums)
            res = [1] * n

            # Left products
            left_product = 1
            for i in range(n):
                res[i] = left_product
                left_product *= nums[i]

            # Right products and final result
            right_product = 1
            for i in range(n - 1, -1, -1):
                res[i] *= right_product
                right_product *= nums[i]

            return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#
