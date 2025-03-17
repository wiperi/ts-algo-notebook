/*
 * @lc app=leetcode.cn id=322 lang=typescript
 *
 * [322] 零钱兑换
 */
// @lc code=start
function coinChange(coins, amount) {
  // 状态转移方程：
  // dp(amount) = 0, 当 amount == 0 时
  // dp(amount) = -1, 当 amount < 0 时
  // dp(amount) = min(dp(amount - coin) + 1), 当 coin <= amount 时
  
  // 题目要求的最终结果是 dp(amount)
  let memo = Array(amount + 1).fill(undefined);
  memo[0] = 0;
  return dp(coins, amount);

  // 定义：要凑出金额 n，至少要 dp(coins, n) 个硬币
  function dp(coins, amount) {
    // base case
    if (amount === 0) return 0;
    if (amount < 0) return -1;

    if (memo[amount] !== undefined) return memo[amount];

    let res = Number.MAX_SAFE_INTEGER;
    for (let coin of coins) {
      // 计算子问题的结果
      let subRes = dp(coins, amount - coin);
      // 子问题无解则跳过
      if (subRes === -1) continue;
      // 在子问题中选择最优解，然后加一
      res = Math.min(res, subRes + 1);
    }

    memo[amount] =  res === Number.MAX_SAFE_INTEGER ? -1 : res;
    return memo[amount];
  }
}
// @lc code=end

if (require.main === module) {
  let res = coinChange([1, 2, 5], 11);
  console.log(res);
}

export {};
