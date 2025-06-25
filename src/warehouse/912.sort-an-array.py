#
# @lc app=leetcode.cn id=912 lang=python3
# @lcpr version=30204
#
# [912] 排序数组
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(lo, hi):

            if (hi - lo + 1) < 2:
                return
            
            mid = (lo + hi) // 2
            mergeSort(lo, mid)
            mergeSort(mid + 1, hi)

            arr = []
            i = lo
            j = mid + 1

            while i <= mid and j <= hi:
                if nums[i] < nums[j]:
                    arr.append(nums[i])
                    i += 1
                else:
                    arr.append(nums[j])
                    j += 1
            
            if i > mid:
                while j <= hi:
                    arr.append(nums[j])
                    j += 1
            else:
                while i <= mid:
                    arr.append(nums[i])
                    i += 1
            
            j = 0
            for i in range(lo, hi + 1):
                nums[i] = arr[j]
                j += 1

        mergeSort(0, len(nums) - 1)
        return nums
# @lc code=end



#
# @lcpr case=start
# [5,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,2,0,0,2]\n
# @lcpr case=end

#

