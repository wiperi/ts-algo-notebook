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

  if (intervals.length === 0) {
    return [];
  }

  let res = [];

  // 简化 overlap 的判定
  intervals.sort((a, b) => {
    return a[0] - b[0];
  });

  let preMin = intervals[0][0];
  let preMax = intervals[0][1];
  let min, max;
  for (let i = 1; i < intervals.length; i++) {
    min = intervals[i][0];
    max = intervals[i][1];

    if (isOverlap(preMin, preMax, min, max)) {
      // merge them
      preMin = Math.min(preMin, min);
      preMax = Math.max(preMax, max);
    } else {
      // update res
      res.push([preMin, preMax]);
      preMin = intervals[i][0];
      preMax = intervals[i][1];
    }
  }

  res.push([preMin, preMax]);

  return res;

  function isOverlap(preMin, preMax, min, max) {
    // preMin always <= min
    if (min >= preMin && min <= preMax) return true;
    if (max >= preMin && max <= preMax) return true;
    return false;
  }
}
// @lc code=end
export {}