/*
 * @lc app=leetcode.cn id=694 lang=typescript
 *
 * [694] 不同的岛屿数量
 */

// @lc code=start
function numDistinctIslands(grid: number[][]) {
  /**
   * If any of two islands have same shape, They must have the same
   * dfs path. On each node, the diretion(order) of when they go into the next
   * valid node is the same. ie. They make the same choice each time.
   */

  const dirs = [
    [1, 0, 'd'], // down
    [0, 1, 'r'], // right
    [0, -1, 'l'], // left
    [-1, 0, 'u'], // up
  ];
  let row = grid.length;
  let col = grid[0].length;

  let used = Array.from({ length: row }, () => Array(col).fill(false));
  let res = 0;

  let path = '';
  let set = new Set();

  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      if (grid[r][c] === 0 || used[r][c]) continue;
      path = '';
      dfs(r, c);
      if (set.has(path)) continue;
      set.add(path);
      console.log(set);
      res++;
    }
  }

  return res;

  function dfs(r, c) {
    if (r < 0 || r >= row || c < 0 || c >= col || used[r][c]) return;
    if (grid[r][c] === 0) return;

    used[r][c] = true;

    for (let [dr, dc, dir] of dirs) {
      path += dir;
      dfs(r + dr, c + dc);
    }
  }
}
// @lc code=end

if (require.main === module) {
  let res = numDistinctIslands([
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
  ]);
  console.log(res);
}
