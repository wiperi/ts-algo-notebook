/*
 * @lc app=leetcode.cn id=2841 lang=typescript
 *
 * [2841] 几乎唯一子数组的最大和
 */

// @lc code=start
function maxSum(nums: number[], m: number, k: number): number {
  // 思路：
  // 维护定长窗口，窗口用set记录独特字符的数量，同时计算窗口和

  let win = new Map<number, number>();
  let winSum = 0;
  let res = 0;
  
  let left = 0, right = k - 1;
  for (let i = left; i <= right; i++) {
    win.set(nums[i], (win.get(nums[i]) || 0) + 1)
    winSum += nums[i];
  }

  if (win.size >= m) {
    res = Math.max(res, winSum);
  }


  right = k;
  while (right < nums.length) {
    if (win.get(nums[left]) === 1) {
      win.delete(nums[left])
    } else {
      win.set(nums[left], win.get(nums[left]) - 1)
    }
    winSum -= nums[left]

    win.set(nums[right], (win.get(nums[right]) || 0) + 1);
    winSum += nums[right]


    if (win.size >= m) {
      res = Math.max(res, winSum);
    }

    left++;
    right++;
  }

  return res;
};
// @lc code=end

if (require.main === module) {
  console.log(maxSum([10,9,7,1,7,6,9,9,9], 3, 3))
}

