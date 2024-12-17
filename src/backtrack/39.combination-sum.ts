/*
 * @lc app=leetcode.cn id=39 lang=typescript
 *
 * [39] 组合总和
 */

// @lc code=start
function combinationSum(candidates: number[], target: number): number[][] {
  let res = [];

  // 记录路径和路径和
  let path = [];
  let pathSum = 0;

  backtrack(0);

  return res;

  function backtrack(start) {

    if (pathSum === target) {
      res.push(path.slice());
      return;
    }

    for (let [i, v] of candidates.entries()) {

      // 组合问题，不可以重复使用同一个元素
      if (i < start) continue;

      // 路径和即将大于 target，跳过
      if (pathSum + v > target) continue;

      pathSum += v;
      path.push(v);
      backtrack(i);
      path.pop();
      pathSum -= v;
    }
  }
}
// @lc code=end

export {}
