/*
 * @lc app=leetcode.cn id=1143 lang=typescript
 *
 * [1143] 最长公共子序列
 */
import _ from 'lodash'
// @lc code=start
function longestCommonSubsequence(s1: string, s2: string): number {
  // dp[i][j] = longestCommonSubsequence(s1[0..i - 1], s2[0..j - 1])
  // i and j are length
  let dp = _.times(s1.length + 1, () => Array(s2.length + 1).fill(0));

  for (let i = 1; i <= s1.length; i++) {
    for (let j = 1; j <= s2.length; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1]  + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  return dp[s1.length][s2.length];
}
// @lc code=end

if (require.main === module) {
  longestCommonSubsequence('','');
}

export {}