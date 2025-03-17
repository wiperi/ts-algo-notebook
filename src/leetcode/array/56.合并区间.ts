/*
 * @lc app=leetcode.cn id=56 lang=typescript
 *
 * [56] 合并区间
 */

// @lc code=start
function merge(intervals: number[][]): number[][] {
  // 伪代码：
  // for (let i = 1; i < intervals.length; i++) {
  //   if (curr overlap with prev) {
  //     merge them
  //   } else {
  //     add prev to res
  //   }
  // }
  // add last one

  intervals.sort((a, b) => {
    return a[0] - b[0];
  })


  let res = [];
  let prev = intervals[0];
  for (let i = 1; i < intervals.length; i++) {
    if (overlap(prev, intervals[i])) {
      prev = [prev[0], Math.max(prev[1], intervals[i][1])];
    } else {
      res.push(prev.slice());
      prev = intervals[i];
    }
  }

  res.push(prev.slice());

  return res;

  function overlap(a, b): boolean {
    if (a[1] >= b[0]) return true
    return false;
  }
};
// @lc code=end


export {}