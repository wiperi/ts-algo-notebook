/*
 * @lc app=leetcode.cn id=79 lang=typescript
 *
 * [79] 单词搜索
 */

// @lc code=start
function exist(board: string[][], word: string): boolean {
  let [row, col] = [board.length, board[0].length];
  let used = Array(row)
    .fill(0)
    .map(() => Array(col).fill(false));
  let found = false;

  for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
      dfs(r, c, 0);
      if (found) return true;
    }
  }

  return false;

  function dfs(r, c, pos) {
    // 坐标越界、走回头路、字符不匹配
    if (r < 0 || r >= row || c < 0 || c >= col || used[r][c] || board[r][c] !== word[pos]) {
      return;
    }

    if (pos === word.length - 1) {
      found = true;
      return;
    }

    used[r][c] = true;
    dfs(r + 1, c, pos + 1);
    dfs(r - 1, c, pos + 1);
    dfs(r, c + 1, pos + 1);
    dfs(r, c - 1, pos + 1);
    used[r][c] = false;
  }
}
// @lc code=end
export {};
