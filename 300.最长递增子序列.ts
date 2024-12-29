/*
 * @lc app=leetcode.cn id=300 lang=typescript
 *
 * [300] 最长递增子序列
 */
import _ from "lodash"
// @lc code=start
function lengthOfLIS(nums: number[]): number {
  // let f(x) = lengthOfLIS from xth element to end
  // f(i) = max(f(j)) for j < i and num[j] < num[i]


  let dp = Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[j] + 1, dp[i]);
      }
    }
  }

  return _.max(dp);
};
// @lc code=end

