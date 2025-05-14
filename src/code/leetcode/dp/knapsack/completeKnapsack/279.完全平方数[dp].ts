/*
 * @lc app=leetcode.cn id=279 lang=typescript
 *
 * [279] 完全平方数
 */

// @lc code=start
function numSquares(n: number): number {
  // state: current n
  // choice: 1 to sqrt(n)
  // state transition: f(n) = min(f(n - 1^2), f(n - 2^2)...)

  let max = 10 ** 6;
  let memo = Array(n + 1).fill(max);

  return dp(n);

  function dp(n) {
    if (memo[n] != 10 ** 6) {
      return memo[n];
    }

    if (n === 0) {
      return 0;
    }

    let res = max;

    for (let i = Math.floor(Math.sqrt(n)); i >= 1; i--) {
      res = Math.min(res, dp(n - i ** 2) + 1);
    }

    memo[n] = res;
    return res;
  }
}
// @lc code=end

export {};

// recur
(function numSquares(n: number): number {
  // state: current n
  // choice: 1 to sqrt(n)
  // state transition: f(n) = min(f(n - 1), f(n - 2)...)

  return dp(n);

  function dp(n) {
    if (n === 0) {
      return 0;
    }

    let res = 10 ** 5;

    for (let i = Math.floor(Math.sqrt(n)); i >= 1; i--) {}

    return res;
  }
});

// iter
(function numSquares(n: number): number {
  let dp = Array(n + 1).fill(Infinity);
  dp[0] = 0;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    for (let j = Math.floor(Math.sqrt(i)); j >= 1; j--) {
      dp[i] = Math.min(dp[i], dp[i - j ** 2] + 1);
    }
  }

  return dp[n];
});
