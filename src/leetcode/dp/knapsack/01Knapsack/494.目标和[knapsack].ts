/*
 * @lc app=leetcode.cn id=494 lang=typescript
 *
 * [494] 目标和
 */

// @lc code=start
function findTargetSumWays(nums: number[], target: number): number {
  // can you pick a subset of nums, that its sum = ((target + sum(nums))) / 2

  const sum = nums.reduce((a, b) => a + b, 0);

  if (sum < Math.abs(target) || (sum + target) % 2 !== 0) {
    // never reach target or (..) / 2 is not a interger
    return 0;
  }

  return subsets((sum + target) / 2);

  // how many subsets in nums having the target sum
  function subsets(sum) {
    
    // dp[i][j] = num of subsets choosed from nums[0..i] having sum of j
    let dp = Array.from({ length: nums.length + 1 }, () => Array(sum + 1).fill(0));

    // base case: there is nothing to choose and the target sum is 0
    dp[0][0] = 1;

    for (let i = 1; i <= nums.length; i++) {
      for (let j = 0; j <= sum; j++) {
        let val = nums[i - 1];

        // can not choose current if current is too big
        if (j < val) {
          dp[i][j] = dp[i - 1][j];
        } else {
          // 2 options: not choose current or choose current
          dp[i][j] = dp[i - 1][j] + dp[i - 1][j - val];
        }
      }
    }

    return dp[nums.length][sum];
  }
}
// @lc code=end

export {};
