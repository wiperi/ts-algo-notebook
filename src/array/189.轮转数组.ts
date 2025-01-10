/*
 * @lc app=leetcode.cn id=189 lang=typescript
 *
 * [189] 轮转数组
 */

// @lc code=start
/**
 Do not return anything, modify nums in-place instead.
 */
 function rotate(nums: number[], k: number): void {

  k = Math.floor(k % nums.length);
  
  reverse(0, nums.length - 1);
  reverse(0, k - 1);
  reverse(k, nums.length - 1)

  return;
  
  function reverse(i, j) {
    while (i < j) {
      [nums[i], nums[j]] = [nums[j], nums[i]]

      i++;
      j--;
    }
  }
};
// @lc code=end

(function rotate(nums: number[], k: number): void {
  // 双指针
  const copy = nums.slice();

  k %= nums.length;

  let i = k;
  
  for (let j = 0; j < nums.length; j++) {
    nums[i++] = copy[j];
    if (i === nums.length) i = 0;
  }
})

