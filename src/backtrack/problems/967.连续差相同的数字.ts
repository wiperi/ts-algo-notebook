/*
 * @lc app=leetcode.cn id=967 lang=typescript
 *
 * [967] 连续差相同的数字
 */

import _ from "lodash";

// @lc code=start
function numsSameConsecDiff(n: number, k: number): number[] {
  // 选择角度：每一位
  // 选择空间：第一位1-9，其他0-9，当前位与前面的位的值相差k

  let path = [];
  let res = [];

  backtrack(0);

  return res.map((arr: number[]) => Number(arr.join('')));

  function backtrack(index) {
    if (index === n) {
      res.push(path.slice());
      return;
    }

    for (let val = 0; val < 10; val++) {
      if (index === 0 && val === 0) continue;

      if (path.length > 0 && Math.abs(_.last(path) - val) !== k) continue;
      path.push(val);
      backtrack(index + 1);
      path.pop();
    }
  }
}
// @lc code=end

if (require.main === module) {
  let res = numsSameConsecDiff(2, 7);
  console.log(res);
}

export {}