/*
 * @lc app=leetcode.cn id=52 lang=typescript
 *
 * [52] N 皇后 II
 */

// @lc code=start
function totalNQueens(n: number): number {
  const columns: Set<number> = new Set();
  const diagonalLeftIncline: Set<number> = new Set();
  const diagonalRightIncline: Set<number> = new Set();
  let res = 0;

  backtrack(0);
  return res;

  function backtrack(row: number): void {
    if (row === n) {
      res++;
      return;
    }

    for (let c = 0; c < n; c++) {
      if (columns.has(c) || diagonalLeftIncline.has(row - c) || diagonalRightIncline.has(row + c)) {
        continue;
      }

      columns.add(c);
      diagonalLeftIncline.add(row - c);
      diagonalRightIncline.add(row + c);
      backtrack(row + 1);
      columns.delete(c);
      diagonalLeftIncline.delete(row - c);
      diagonalRightIncline.delete(row + c);
    }
  }
}
// @lc code=end

export {}