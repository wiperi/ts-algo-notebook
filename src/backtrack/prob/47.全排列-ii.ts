/*
 * @lc app=leetcode.cn id=47 lang=typescript
 *
 * [47] 全排列 II
 */

// @lc code=start
function permuteUnique(nums: number[]): number[][] {
  let res = [];
  let path = [];
  let usedIndex = Array(nums.length).fill(false);

  nums.sort();
  backtrack();

  return res;

  function backtrack() {

    if (path.length === nums.length) {
      res.push(path.slice());
      return;
    }

    for (let [i, v] of nums.entries()) {
      // 排列问题， 元素不可重复使用
      if (usedIndex[i] === true) continue;

      if (i > 0 && nums[i] == nums[i - 1]) {
        // 如果当前元素是一个重复元素，如[1, 1', 1'']中的1'
        if (usedIndex[i - 1] === false) {
          // 且前一个元素没有被使用过，1没有被使用过
          continue;
        }
      }

      // 如果当前元素是重复元素，此时前一个元素已经被使用过
      // 例如，只有当1被使用之后，1'才能被使用
      // 确保重复元素们之间的相对顺序和原数组中的相对顺序一致
      // 如，1'只能再1之后被使用，1''只能再1'之后被使用

      path.push(v);
      usedIndex[i] = true;
      backtrack();
      usedIndex[i] = false;
      path.pop();
    }
  }
}

// @lc code=end
