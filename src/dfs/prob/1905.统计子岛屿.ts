/*
 * @lc app=leetcode.cn id=1905 lang=typescript
 *
 * [1905] 统计子岛屿
 */

// @lc code=start
function countSubIslands(grid1: number[][], grid2: number[][]): number {
  /**
   * Reverse thinking, for islands in grid2, if any cell has a 0 counterpart
   * in grid1, then that whole island is not a sub island.
   */
  
  let row = grid2.length;
  let col = grid2[0].length;

  let used = Array.from({ length: row }, () => Array(col).fill(false));
  let isSubIsland = true;
  let res = 0;

  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      if (grid2[r][c] === 0 || used[r][c]) continue;
      isSubIsland = true;
      dfs(r, c);
      if (isSubIsland) res++;
    }
  }

  return res;

  function dfs(r, c) {
    if (r < 0 || r >= row || c < 0 || c >= col || used[r][c]) return;
    if (grid2[r][c] === 0) return;
    
    if (grid1[r][c] === 0) isSubIsland = false;
    used[r][c] = true;

    dfs(r + 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
    dfs(r - 1, c);
  }
}
// @lc code=end
