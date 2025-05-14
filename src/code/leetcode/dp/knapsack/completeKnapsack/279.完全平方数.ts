/*
 * @lc app=leetcode.cn id=279 lang=typescript
 *
 * [279] 完全平方数
 */

// @lc code=start
function numSquares(n: number): number {
  // choose subset from [1..sqrt(n)]
  // sum of val^2 = no
  // you can choose same element multiple times

  return dp(Math.floor(Math.sqrt(n)), n);

  function dp(i, amount) {
    if (amount === 0) {
      return 0;
    }

    if (i === 0) {
      return Number.MAX_SAFE_INTEGER;
    }

    let val = i ** 2;

    if (val > amount) {
      // can't not choose current coin
      return dp(i - 1, amount);
    } else {
      // 2 options: don't choose current coin, or choose current coin (you can choose current coin multiple times)
      return Math.min(dp(i - 1, amount), dp(i, amount - val) + 1);
    }
  }
}
// @lc code=end

export {}