/*
 * @lc app=leetcode.cn id=40 lang=typescript
 *
 * [40] 组合总和 II
 */

// @lc code=start
function combinationSum2(candidates: number[], target: number): number[][] {
  let res = [];
  let path = [];
  let pathSum = 0
  
  candidates.sort();
  backtrack(0);

  return res;

  function backtrack(start) {

    if (pathSum === target) {
      res.push(path.slice());
      return;
    }

    for (let [i, v] of candidates.entries()) {
      
      if (i < start) continue;
      if (i > start && candidates[i] === candidates[i - 1]) continue;
      if (pathSum + v > target) continue;

      path.push(v);
      pathSum += v;
      backtrack(i + 1);
      pathSum -= v;
      path.pop();
    }
  }
};
// @lc code=end

