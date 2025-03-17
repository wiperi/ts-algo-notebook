/*
 * @lc app=leetcode.cn id=198 lang=typescript
 *
 * [198] 打家劫舍
 */

// @lc code=start
function rob(nums: number[]): number {
  // 状态：目前抢到第几家了
  // 选择：隔1家抢还是隔2家抢

  // 状态转移：
  // input: [a,b,c,d,e]
  // f([a..e]) = max(f([c..e]), f([d,e])) + a

  return Math.max(dp(0, 0), dp(1, 0));

  function dp(index, money): number {
    if (index >= nums.length) return money;

    let res = 0;
    for (let di of [2, 3]) {
      res = Math.max(res, dp(index + di, money + nums[index]));
    }

    return res;
  }
}
// @lc code=end

if (require.main === module) {
  let res = rob([2,1,1,2])
  console.log(res);
}
export {}