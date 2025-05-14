/*
 * @lc app=leetcode.cn id=518 lang=typescript
 *
 * [518] 零钱兑换 II
 */

// @lc code=start
function change(amount: number, coins: number[]): number {

  let dp = Array.from({ length: coins.length + 1 }, () => Array(amount + 1).fill(0));

  for (let i = 0; i <= coins.length; i++) {
    dp[i][0] = 1;
  }
  dp[0][0] = 0;

  for (let i = 1; i <= coins.length; i++) {
    for (let j = 1; j <= amount; j++) {
      let val = coins[i - 1];

      if (val > j) {
        dp[i][j] = dp[i - 1][j];
      } else {
        dp[i][j] = dp[i - 1][j] + dp[i][j - val];
      }
    }
  }

  return dp[coins.length][amount];
}
// @lc code=end

// 递归
(function change(amount: number, coins: number[]): number {
  return dp(coins.length, amount);

  /**
   * 状态：
   * 前i个元素，目标金额
   *
   * 选择：
   * 选还是不选
   *
   * 子问题：
   * 选，i不变（因为可以接着选当前元素），amount变小
   * 不选，i变小，amount不变
   */
  function dp(i, amount) {
    if (i === 0) return 0;

    if (amount === 0) return 1;

    if (amount < 0) return 0;

    const val = coins[i - 1];
    return dp(i, amount - val) + dp(i - 1, amount);
  }
});

export {}