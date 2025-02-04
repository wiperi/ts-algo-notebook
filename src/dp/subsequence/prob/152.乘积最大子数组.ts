/*
 * @lc app=leetcode.cn id=152 lang=typescript
 *
 * [152] 乘积最大子数组
 */

// @lc code=start
function maxProduct(nums: number[]): number {
  // space compression

  let maxdp_prev = nums[0];
  let mindp_prev = nums[0];
  let mindp;
  let maxdp;
  let res = nums[0];

  for (let i = 1; i < nums.length; i++) {
    mindp = Math.min(nums[i], mindp_prev * nums[i], maxdp_prev * nums[i]);
    maxdp = Math.max(nums[i], maxdp_prev * nums[i], mindp_prev * nums[i]);

    mindp_prev = mindp;
    maxdp_prev = maxdp;

    res = Math.max(res, maxdp);
  }

  return res;
}
// @lc code=end

(function maxProduct(nums: number[]): number {
  // state: nums length
  // choice: choose or not choose
  // state transition:
  // since there is negative number
  // so dp[i] = max(nums[i], prev max val * nums[i], prev min val * nums[i])
  
  // dp[i] = the max / min product of a sub array ending with nums[i]
  let maxdp = nums.slice();
  let mindp = nums.slice();
  
  for (let i = 1; i < nums.length; i++) {
    mindp[i] = Math.min(nums[i], mindp[i - 1] * nums[i], maxdp[i - 1] * nums[i]);
    maxdp[i] = Math.max(nums[i], maxdp[i - 1] * nums[i], mindp[i - 1] * nums[i]);
  }
  
  return _.max(maxdp);});
