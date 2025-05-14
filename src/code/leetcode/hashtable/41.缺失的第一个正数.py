#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30104
#
# [41] 缺失的第一个正数
#
from typing import List


# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # https://leetcode.cn/problems/first-missing-positive/solutions/7703/tong-pai-xu-python-dai-ma-by-liweiwei1419

        # The important is to notcie the answer has to be in [1, n + 1], n = len(nums).
        # Because if you have n elements, as long as they are not strictly continuous increasing, eg. 1,2,3,4
        # You would have a gap between [1, n]
        # And even you have a strictly continuous increasing sequence, the answer will be n + 1

        # Then we need to build a in-place hash table. Map from i -> i + 1
        # So, we have index from 0 to n - 1 means we can have a hash table from 1 to n

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        # Build the hash table
        n = len(nums)
        for i in range(n):

            # While nums[i] should be in the hash table and it is not in the correct place
            # Swap it to the correct place
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i] - 1)

        # Check existence for [1, n], if there is any gap, then the gap is the answer
        # Otherwise, the answer will be n + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


# @lc code=end


class BruteForce:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Handle empty array or arrays with only non-positive numbers
        if not nums or max(nums) <= 0:
            return 1

        s = {n for n in nums}

        # Start from 1 since we're looking for the first missing positive integer
        for n in range(1, max(nums) + 2):
            if n not in s:
                return n

        return max(nums) + 1


#
# @lcpr case=start
# [1, 1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#
