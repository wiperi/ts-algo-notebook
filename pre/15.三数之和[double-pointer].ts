/*
 * @lc app=leetcode.cn id=15 lang=typescript
 *
 * [15] 三数之和
 */

// @lc code=start
function threeSum(nums: number[]): number[][] {

  nums.sort((a, b) => a - b);
  let res = [];
  
  for (let i = 0; i < nums.length - 1; i++) {

    // 跳过重复元素
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    
    let twoSumResArr = twoSum(i + 1, 0 - nums[i]);
    if (twoSumResArr.length === 0) continue;

    for (let twoSumRes of twoSumResArr) {
      twoSumRes.push(nums[i]);
      res.push(twoSumRes);
    }
  }

  return res;

  function twoSum(start: number, target: number): number[][] {
    let lo = start, hi = nums.length - 1;
    let res = [];
    while (lo < hi) {
      let sum = nums[lo] + nums[hi];
      if (sum < target) {
        lo++;
      } else if (sum > target) {
        hi--;
      } else {
        res.push([nums[lo], nums[hi]]);

        // 跳过重复元素
        while (lo < hi && nums[lo] == nums[++lo]) continue;
        while (lo < hi && nums[hi] == nums[--hi]) continue;
      }
    }
    return res;
  }
};
// @lc code=end

export {};
