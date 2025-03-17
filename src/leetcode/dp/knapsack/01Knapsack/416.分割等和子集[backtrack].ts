/*
 * @lc app=leetcode.cn id=416 lang=typescript
 *
 * [416] 分割等和子集
 */

// @lc code=start
function canPartition(nums: number[]): boolean {
  // state: how many number are settled
  // choice: go to bucket 0 or bucket 1

  let b = [0, 0];
  let res = false;
  backtrack(0);

  return res;
  
  function backtrack(i) {
    if (res === true) return;


    if (i === nums.length) {
      if (b[0] === b[1]) {
        res = true;
      }
      return
    }
    
    b[0] += nums[i];
    backtrack(i + 1);
    b[0] -= nums[i];

    b[1] += nums[i];
    backtrack(i + 1)
    b[1] -= nums[i];
  }
};
// @lc code=end

export {}
