/*
 * @lc app=leetcode.cn id=322 lang=typescript
 *
 * [322] 零钱兑换
 */

// @lc code=start
function coinChange(coins: number[], amount: number): number {
  let IMPOSSIBLE = Number.MAX_SAFE_INTEGER;
  let dp = Array(amount + 1).fill(IMPOSSIBLE);
  dp[0] = 0;

  for (let amt = 0; amt <= amount; amt++) {

    for (const coin of coins) {
      if (amt - coin < 0) continue;
      dp[amt] = Math.min(dp[amt], 1 + dp[amt - coin]);
    }
    
  }

  return dp[amount] === IMPOSSIBLE ? -1 : dp[amount];
}
// @lc code=end

export {};
