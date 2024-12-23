/*
 * @lc app=leetcode.cn id=300 lang=typescript
 *
 * [300] 最长递增子序列
 */

import _ from 'lodash';

// @lc code=start
function lengthOfLIS(nums: number[]): number {
  // 对于 [a, b, c, d]，令 f(x) 为 [first..x] 的最长递增子序列的长度
  // f(a) = 1
  // f(c) = max(f(m), 1)，其中 m < c 且 m 在 [a, b] 中

  let dp = Array(nums.length).fill(1);

  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] >= nums[i]) continue;

      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }

  return _.max(dp);
}
// @lc code=end

if (require.main === module) {
  let res = lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]);
  console.log(res);
}
