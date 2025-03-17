/*
 * @lc app=leetcode.cn id=72 lang=typescript
 *
 * [72] 编辑距离
 */

import _ from 'lodash'

// @lc code=start
function minDistance(s1: string, s2: string): number {

  // dp[i][j] = minDistance(s1[0..i + 1], s2[0..j + 1])
  let dp = Array.from({ length: s1.length + 1 }, () =>
    Array.from({ length: s2.length + 1 }, () => 0)
  );

  dp.forEach((_, i) => {
    dp[i][0] = i;
  });
  dp[0].forEach((_, i) => {
    dp[0][i] = i;
  });

  for (let i = 1; i <= s1.length; i++) {
    for (let j = 1; j <= s2.length; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
      }
    }
  }

  return dp[s1.length][s2.length];
}
// @lc code=end

if (require.main === module) {
  let res = minDistance('', 'a');
  console.log(res);
}

export {};
