function solveSudoku(board) {
  let index = 0;
  let halt = false;

  backtrack();

  return;

  function backtrack() {
    let floor = Math.floor;
    let [r, c] = [floor(index / 9), floor(index % 9)];

    // is solution?
    if (index === 9 * 9) {
      halt = true;
      return;
    }

    // prune
    if (board[r][c] !== '.') {
      index++;
      backtrack();
      index--;
      return;
    }

    for (let val = 1; val <= 9; val++) {
      // prune
      if (!isValid(r, c, val)) continue;

      // update
      index++;
      board[r][c] = String(val);

      // make choice
      backtrack();

      // only need to find one solution
      if (halt) return;

      // undo
      board[r][c] = '.';
      index--;
    }
  }

  function isValid(r, c, val) {
    for (let i = 0; i < 9; i++) {
      // 判断行是否存在重复
      if (board[r][i] === val) return false;
      // 判断列是否存在重复
      if (board[i][c] === val) return false;
      // 判断 3 x 3 方框是否存在重复
      if (
        board[Math.floor(r / 3) * 3 + Math.floor(i / 3)][Math.floor(c / 3) * 3 + (i % 3)] === val
      ) {
        return false;
      }
    }
    return true;
  }
}

if (require.main === module) {
  let board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
  ];

  solveSudoku(board);

  for (let row of board) {
    console.log(row);
  }
}
