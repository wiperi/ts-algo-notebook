/*
 * @lc app=leetcode.cn id=322 lang=typescript
 *
 * [322] 零钱兑换
 */

// Recursive
function coinChange(coins: number[], amount: number): number {
  // Assume f(0)..f(n - 1) is known.
  // How about f(n).
  // f(n) = min(f(n - coin 1), f(n - coin 2)...f(n - coin N)) + 1;

  return dp(amount);

  function dp(n): number {
    if (n < 0) return -1;
    if (n == 0) return 0;

    let res = Infinity;

    for (let coin of coins) {
      if (dp(n - coin) === -1) continue;
      res = Math.min(res, dp(n - coin) + 1);
    }

    return res == Infinity ? -1 : res;
  }
}

// Recursive + Memo
{
  // @lc code=start
  function coinChange(coins: number[], amount: number): number {

    let memo = Array(amount).fill(undefined);

    return dp(amount);

    function dp(n): number {
      if (n < 0) return -1;
      if (n == 0) return 0;

      if (memo[n] != undefined) return memo[n];

      let res = Infinity;

      for (let coin of coins) {
        if (dp(n - coin) === -1) continue;
        res = Math.min(res, dp(n - coin) + 1);
      }

      memo[n] = res == Infinity ? -1 : res;
      return memo[n];
    }
  }
  // @lc code=end
}

export {};
