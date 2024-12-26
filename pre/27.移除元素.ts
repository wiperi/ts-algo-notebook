/*
 * @lc app=leetcode.cn id=27 lang=typescript
 *
 * [27] 移除元素
 */

// @lc code=start
function removeElement(nums: number[], val: number): number {
  let left = 0;
  let right = nums.length;

  while (left < right) {
    if (nums[left] === val) {
      nums[left] = nums[right - 1];
      right--;
    } else {
      left++;
    }
  }

  return left;

  function swap(i: number, j: number): void {
    [nums[i], nums[j]] = [nums[j], nums[i]];
  }
}
// @lc code=end

if (require.main === module) {
  console.log(removeElement([3,2,2,3], 3));
}
