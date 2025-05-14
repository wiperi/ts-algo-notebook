/*
 * @lc app=leetcode.cn id=980 lang=typescript
 *
 * [980] 不同路径 III
 */

import _ from 'lodash';

// @lc code=start
const dirs = [
  [0, 1], // right
  [1, 0], // down
  [0, -1], // left
  [-1, 0], // up
];

function uniquePathsIII(grid: number[][]): number {
  // 状态：当前位置，已走过的路径
  // 选择：4个方向中合法的那个格子
  // 剪枝：不能走回头路，不能走出界外

  let res = 0;
  let [row, col] = [grid.length, grid[0].length];
  let used = _.times(row, () => Array(col).fill(false));

  let start,
    end,
    numValidSquare = 0;

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (grid[i][j] === 1) {
        start = [i, j];
        used[i][j] = true; // 标记出发点，因为标记行为定义在backtrack内部前序位置，递归中无法标记根节点
      } else if (grid[i][j] === 2) {
        end = [i, j];
        numValidSquare++;
      } else if (grid[i][j] === -1) {
        used[i][j] = true;
      } else {
        numValidSquare++;
      }
    }
  }

  backtrack(start[0], start[1]);

  return res;

  function backtrack(r, c) {
    if (r === end[0] && c === end[1] && numValidSquare === 0) {
      res++;
      return;
    }

    for (let [dr, dc] of dirs) {
      let newR = r + dr;
      let newC = c + dc;

      if (newR < 0 || newR >= row || newC < 0 || newC >= col) continue;
      if (used[newR][newC] === true) continue;

      used[newR][newC] = true;
      numValidSquare--;
      backtrack(r + dr, c + dc);
      numValidSquare++;
      used[newR][newC] = false;
    }
  }
}
// @lc code=end

if (require.main === module) {
  let res = uniquePathsIII([
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 2, -1],
  ]);
  console.log(res);
}

export {}