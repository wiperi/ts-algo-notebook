// import _ from 'lodash';
/*
 * @lc app=leetcode.cn id=1254 lang=typescript
 *
 * [1254] 统计封闭岛屿的数目
 */

// @lc code=start
function closedIsland(grid: number[][]): number {
  /**
   * for all 0 in mattrix, do a dfs, if reach the boundary, then is not a island
   *
   * after all iteration , if it doesn't reach the boundary, then it is a island
   */

  let row = grid.length;
  let col = grid[0].length;

  let used = _.times(row, () => Array(col).fill(false));
  let res = 0;
  let isIsland = true;

  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      if (grid[r][c] === 1 || used[r][c]) continue;
      isIsland = true;
      dfs(r, c);
      if (isIsland) res++;
    }
  }

  return res;

  function dfs(r, c) {
    if (r < 0 || r >= row || c < 0 || c >= col) {
      isIsland = false;
      return;
    }

    if (grid[r][c] === 1 || used[r][c]) return;

    used[r][c] = true;

    dfs(r + 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
    dfs(r - 1, c);
  }
}
// @lc code=end
if (require.main === module) {
  closedIsland([
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
  ]);
}
