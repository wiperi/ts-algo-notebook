/*
 * @lc app=leetcode.cn id=516 lang=typescript
 *
 * [516] 最长回文子序列
 */
import _ from 'lodash';
// @lc code=start
function longestPalindromeSubseq(s: string) {
  // dp[i][j] = length of longestPalindrome of s[i..j]
  let dp = _.times(s.length, () => Array(s.length).fill(0));
  dp.forEach((_, i) => {
    dp[i][i] = 1;
  });

  for (var i = s.length - 1; i >= 0; i--) {
    for (var j = i + 1; j < s.length; j++) {
      // 状态转移方程
      if (s.charAt(i) === s.charAt(j)) {
        dp[i][j] = dp[i + 1][j - 1] + 2;
      } else {
        dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
      }
    }
  }

  return dp[0][s.length - 1];
}
// @lc code=end

if (require.main === module) {
  let res = longestPalindromeSubseq('bbbab');
  console.log(res);
}

export {}