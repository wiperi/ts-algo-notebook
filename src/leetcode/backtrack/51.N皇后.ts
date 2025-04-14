/*
 * @lc app=leetcode id=51 lang=typescript
 *
 * [51] N-Queens
 */

// @lc code=start
function solveNQueens(n: number): string[][] {
  const board = Array(n)
    .fill(0)
    .map(() => '.'.repeat(n));
  let res = [];

  backtrack(0);

  return res;

  function backtrack(r) {
    if (r === n) {
      res.push([...board]);
      return;
    }

    for (let c = 0; c < n; c++) {
      if (!isValid(r, c)) continue;

      board[r] = board[r].substring(0, c) + 'Q' + board[r].substring(c + 1);
      backtrack(r + 1);
      board[r] = board[r].substring(0, c) + '.' + board[r].substring(c + 1);
    }
  }

  function isValid(r, c) {
    // 检查列
    for (let i = 0; i < r; i++) {
      if (board[i][c] === 'Q') return false;
    }

    // 检查左上对角线
    for (let i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--) {
      if (board[i][j] === 'Q') return false;
    }

    // 检查右上对角线
    for (let i = r - 1, j = c + 1; i >= 0 && j < n; i--, j++) {
      if (board[i][j] === 'Q') return false;
    }

    return true;
  }
}

if (require.main === module) {
  let res = solveNQueens(4);

  for (const board of res) {
    for (const row of board) {
      console.log(row.split('').join(' '));
    }
    console.log();
  }
}
// @lc code=end

export {};
