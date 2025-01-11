/*
 * @lc app=leetcode.cn id=518 lang=typescript
 *
 * [518] 零钱兑换 II
 */

// @lc code=start
function change(amount: number, coins: number[]): number {
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
}
// @lc code=end
