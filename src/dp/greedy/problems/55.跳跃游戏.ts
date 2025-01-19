/*
 * @lc app=leetcode.cn id=55 lang=typescript
 *
 * [55] 跳跃游戏
 */

// @lc code=start
function canJump(nums: number[]): boolean {
  let canReach = 0;

  for (let pos = 0; pos < nums.length; pos++) {
    if (canReach < pos) return false;
    canReach = Math.max(canReach, pos + nums[pos]);
  }

  if (canReach >= nums.length - 1) return true;
};

// @lc code=end

// dp
(function canJump(nums: number[]): boolean {
  // state: pos
  // choice: each pos that in jump range

  return dp(0);

  function dp(p) {
    if (p >= nums.length - 1) return true;

    for (let i = p + 1; i <= p + nums[p]; i++) {
      if (dp(i) === true) return true;
    }

    return false;
  }
})
