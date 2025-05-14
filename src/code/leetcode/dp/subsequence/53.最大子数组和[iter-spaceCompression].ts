/*
 * @lc app=leetcode.cn id=53 lang=typescript
 *
 * [53] 最大子数组和
 */
import _ from 'lodash'

// @lc code=start
function maxSubArray(nums: number[]): number {
  // space compression version

  // let f(x) be maxSubArray(nums[x..end])
  // for f(x - 1), there are 2 options
  // 1. include current nums[x - 1]
  // 2. not include current nums[x - 1]
  // f(x - 1) = max(f(x), f(x) + nums[x - 1])

  let dp_i, dp_i_1;
  dp_i_1 = nums[0];
  let res = dp_i_1;
  
  for (let i = 1; i < nums.length; i++) {
    dp_i = Math.max(nums[i], dp_i_1 + nums[i]);
    res = Math.max(res, dp_i);
    dp_i_1 = dp_i;
  }

  return res;
};
// @lc code=end

if (require.main === module) {
  maxSubArray([1,2,3])
}

(function maxSubArray(nums: number[]): number {
  // simple verson

  // let f(x) be maxSubArray(nums[x..end])
  // for f(x - 1), there are 2 options
  // 1. include current nums[x - 1]
  // 2. not include current nums[x - 1]
  // f(x - 1) = max(f(x), f(x) + nums[x - 1])

  let dp = Array(nums.length).fill(0);
  dp[0] = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
  }

  return _.max(dp);
})

export {}