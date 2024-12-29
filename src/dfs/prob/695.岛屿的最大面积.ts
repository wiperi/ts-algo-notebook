/*
 * @lc app=leetcode.cn id=695 lang=typescript
 *
 * [695] 岛屿的最大面积
 */

// @lc code=start
function maxAreaOfIsland(grid: number[][]): number {
  let row = grid.length;
  let col = grid[0].length;

  let used = Array.from({ length: row }, () => Array(col).fill(false));
  let res = 0;
  let area = 0;

  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      if (grid[r][c] === 0 || used[r][c]) continue;
      area = 0;
      dfs(r, c);
      res = Math.max(res, area);
    }
  }

  return res;

  function dfs(r, c) {
    if (r < 0 || r >= row || c < 0 || c >= col || used[r][c]) return;
    if (grid[r][c] === 0) return;

    used[r][c] = true;
    area++;

    dfs(r + 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
    dfs(r - 1, c);
  }
}
// @lc code=end
