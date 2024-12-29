/*
 * @lc app=leetcode.cn id=1143 lang=typescript
 *
 * [1143] 最长公共子序列
 */

// @lc code=start
function longestCommonSubsequence(s1: string, s2: string): number {
  // let f(i, j) = longestCommonSubsequence(s1[0..i], s2[0..j])

  let memo = _.times(s1.length, () => Array(s2.length).fill(-1));

  return dp(0, 0);

  function dp(i, j) {

    if (i >= s1.length || j >= s2.length) return 0;

    if (memo[i][j] !== -1) return memo[i][j];

    if (s1[i] === s2[j]) {
      memo[i][j] =  dp(i + 1, j + 1) + 1;
    } else {
      memo[i][j] =  Math.max(dp(i, j + 1), dp(i + 1, j));
    }

    return memo[i][j];
  }
}
// @lc code=end

if (require.main === module) {
  longestCommonSubsequence('','');
}

(function longestCommonSubsequence(s1: string, s2: string): number {
  // let f(i, j) = longestCommonSubsequence(s1[i..end], s2[j..end])

  return dp(0, 0);

  function dp(i, j) {

    if (i >= s1.length || j >= s2.length) return 0;

    if (s1[i] === s2[j]) {
      // match next char
      return dp(i + 1, j + 1) + 1;
    } else {
      // discard s1[i] or s2[j]
      return Math.max(dp(i, j + 1), dp(i + 1, j));
    }
  }
})
