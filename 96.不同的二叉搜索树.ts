/*
 * @lc app=leetcode.cn id=96 lang=typescript
 *
 * [96] 不同的二叉搜索树
 */

// @lc code=start
function numTrees(n: number): number {
    // const dp: number[] = new Array(n + 1).fill(0);
    // dp[0] = 1;
    // dp[1] = 1;

    // for (let i = 2; i <= n; i++) {
    //   for (let j = 0; j < i; j++) {
    //     dp[i] += dp[j] * dp[i - j - 1];
    //   }
    // }

    // return dp[n];

    return permute(Array(n).fill(0).map((v, i) => i + 1)).length;
};

function permute(nums: number[]): number[][] {
  let res = [];
  let path = [];

  backtrack();

  return res;

  function backtrack() {
    
    if (path.length === nums.length) {
      res.push(path.slice());
      return;
    }

    for (let [i, v] of nums.entries()) {
      if (path.includes(v)) continue;

      path.push(v);
      backtrack();
      path.pop();
    }
  }
}
// @lc code=end

