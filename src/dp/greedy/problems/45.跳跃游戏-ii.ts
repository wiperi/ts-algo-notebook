/*
 * @lc app=leetcode.cn id=45 lang=typescript
 *
 * [45] 跳跃游戏 II
 */

// @lc code=start
function jump(nums: number[]): number {
  // 链接：
  // https://leetcode.cn/problems/jump-game-ii/solutions/9347/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/

  // end记录跳跃边界，每次达到条约边界，就记录一次跳跃。
  let canReach = 0;
  let jump = 0;
  let end = 0;

  for (let pos = 0; pos < nums.length - 1; pos++) {
    canReach = Math.max(canReach, pos + nums[pos]);

    if (pos === end) {
      jump++;
      end = canReach;
    }
  }

  return jump;


}
// @lc code=end

(function jump(nums: number[]): number {

  return dp(0);
  

  function dp(p) {
    if (p >= nums.length - 1) return 0;

    let res = Number.MAX_SAFE_INTEGER;

    for (let i = p + 1; i <= p + nums[p]; i++) {
      res = Math.min(res, 1 + dp(i));
    }

    return res;
  }
})
