/*
 * @lc app=leetcode.cn id=70 lang=typescript
 *
 * [70] 爬楼梯
 */

// @lc code=start
function climbStairs(n: number): number {
  let memo = Array(n + 1);
  return numWays(n);

  function numWays(step) {
    if (step === 1) return 1;
    if (step === 2) return 2;

    if (memo[step]) return memo[step];

    memo[step] = numWays(step - 1) + numWays(step - 2);

    return memo[step];
  }
}
// @lc code=end

if (require.main === module) {
  for (let i = 1; i < 10; i++) {
    let res = climbStairs(i);
    console.log(res);
  }
}

export {};
