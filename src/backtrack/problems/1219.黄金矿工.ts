/*
 * @lc app=leetcode.cn id=1219 lang=typescript
 *
 * [1219] 黄金矿工
 */
import _ from 'lodash';
// @lc code=start

let dirs = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

function getMaximumGold(grid: number[][]): number {
  // state: location
  // choices: 4 direction

  let row = grid.length;
  let col = grid[0].length;

  let maxPathSum = 0;
  let pathSum = 0;
  // if a spot used in current path
  let inPath = _.times(row, () => Array(col).fill(false));
  // if a spot ever touched
  let touched = _.times(row, () => Array(col).fill(false));

  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      if (grid[r][c] === 0) continue;
      if (touched[r][c] === true) continue;

      touched[r][c] = true;
      dfs(r, c);
    }
  }

  return maxPathSum;

  function dfs(r, c) {

    if (r < 0 || r >= row || c < 0 || c >= col) return;
    if (grid[r][c] === 0) return;
    if (inPath[r][c] === true) return;

    inPath[r][c] = true;
    pathSum += grid[r][c];
    maxPathSum = Math.max(maxPathSum, pathSum);

    for (let [dr, dc] of dirs) {
      dfs(r + dr, c + dc);
    }

    pathSum -= grid[r][c];
    inPath[r][c] = false;
  }
}
// @lc code=end

if (require.main === module) {
  let input = [
    [1, 0, 7],
    [2, 0, 6],
    [3, 4, 5],
    [0, 3, 0],
    [9, 0, 20],
  ];
  let res = getMaximumGold(input);
  console.log(input);
  console.log(res);
}

export {}