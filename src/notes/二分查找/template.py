from bisect import bisect_left, bisect_right
from math import inf


def rightBound(nums: list[int], target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        v = nums[mid]

        if target >= v:
            l = mid + 1
        else:
            r = mid

    return r


def leftBound(nums: list[int], target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        v = nums[mid]

        if target <= v:
            r = mid
        else:
            l = mid + 1

    return r


# 在数组中查找 x 左右两端元素和 x 的最小高度差
def findDistance(nums: list[int], target):
    nums = [-inf] + nums + [inf]
    r = bisect_right(nums, target)
    l = r - 1
    leftSideDifference = target - nums[l]
    rightSideDifference = nums[r] - target

    return min(leftSideDifference, rightSideDifference)

def findDistanceV2(nums: list[int], target):
    r = bisect_right(nums, target)
    l = r - 1

    # nums[l] <= target < nums[r]

    leftSideDifference = (target - nums[l]) if l >= 0 else inf
    rightSideDifference = (nums[r] - target) if r <= len(nums) else inf

    return min(leftSideDifference, rightSideDifference)


bisect_right # 查找第一个 > x 的下标
bisect_left  # 查找第一个 >= x 的下标