/*
 * @lc app=leetcode.cn id=494 lang=typescript
 *
 * [494] 目标和
 */

// @lc code=start
function findTargetSumWays(nums: number[], target: number): number {
  let sum = 0;
  let res = 0;

  backtrack(0);

  return res;

  /**
   * state: how many nubmer are choosen
   * choose: + or -
   */
  function backtrack(i) {
    if (i === nums.length) {
      if (sum === target) {
        res++;
      }
      return;
    }

    sum += nums[i];
    backtrack(i + 1);
    sum -= nums[i];

    sum -= nums[i];
    backtrack(i + 1);
    sum += nums[i];
  }
}
// @lc code=end

export {}