#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30204
#
# [31] 下一个排列
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def reverse(i, j):
            while i < j and nums[i] > nums[j]:
                swap(i, j)
                i += 1
                j -= 1

        n = len(nums)
        i, j = n - 2, n - 1
        while i >= 0:
            if nums[i] < nums[j]:
                for k in range(j, n):
                    if nums[k] <= nums[i]:
                        k -= 1
                        break
                swap(i, k)
                # print(nums, i, k)
                reverse(i + 1, n - 1)
                # print(nums)
                
                return

            i -= 1
            j -= 1
        
        nums.sort()


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,5,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#
