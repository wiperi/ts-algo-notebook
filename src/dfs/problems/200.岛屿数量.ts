/*
 * @lc app=leetcode.cn id=200 lang=typescript
 *
 * [200] 岛屿数量
 */

// @lc code=start
function numIslands(grid: string[][]): number {
  let row = grid.length;
  let col = grid[0].length;

  let used = _.times(row, () => Array(col).fill(false));
  let res = 0;

  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      if (grid[r][c] === '0' || used[r][c]) continue;
      res++;
      dfs(r, c);
    }
  }

  return res;

  function dfs(r, c) {
    if (r < 0 || r >= row || c < 0 || c >= col || used[r][c]) return;
    if (grid[r][c] === '0') return;

    used[r][c] = true;
    dfs(r + 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
    dfs(r - 1, c);
  }
}
// @lc code=end

export {}