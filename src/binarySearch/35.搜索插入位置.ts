/*
 * @lc app=leetcode.cn id=35 lang=typescript
 *
 * [35] 搜索插入位置
 */

// @lc code=start
function searchInsert(nums: number[], target: number): number {

  let lo = 0
  let hi = nums.length - 1
  let m: number;

  while (lo <= hi) {
    m = mid(lo, hi);

    if (nums[m] === target) {
      return m;
    } else if (nums[m] < target) {
      lo = m + 1;
    } else {
      hi = m - 1;
    }
  }

  // 此时只有两种情况
  // target > mid val, lo = hi + 1
  // tar < mid val, hi = lo - 1
  // 这两种情况下，都应该返回 lo
  return lo;

  function mid(a: number, b: number) {
    return Math.floor((a + b) / 2)
  }
};
// @lc code=end

