/*
 * @lc app=leetcode.cn id=516 lang=typescript
 *
 * [516] 最长回文子序列
 */

// @lc code=start
var longestPalindromeSubseq = function(s) {
  var n = s.length;
  // dp 数组全部初始化为 0
  var dp = new Array(n).fill(0).map(x => new Array(n).fill(0));
  // base case
  for (var i = 0; i < n; i++) {
      dp[i][i] = 1;
  }

  console.log(dp)

  // 反着遍历保证正确的状态转移
  for (var i = n - 1; i >= 0; i--) {
      for (var j = i + 1; j < n; j++) {
          // 状态转移方程
          if (s.charAt(i) === s.charAt(j)) {
              dp[i][j] = dp[i + 1][j - 1] + 2;
          } else {
              dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
          }
          let temp = dp[i][j];
          dp[i][j] = `${dp[i][j]}*`
          console.log(dp)
          dp[i][j] = temp
      }
  }
  // 整个 s 的最长回文子串长度
  return dp[0][n - 1];
};
// @lc code=end

if (require.main === module) {
  let res = longestPalindromeSubseq('bbbab');
  console.log(res)
}

