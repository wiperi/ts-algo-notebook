function solveSudoku(board) {
  let index = 0;
  let halt = false;

  backtrack();

  return;

  function backtrack() {
    let floor = Math.floor;
    let [r, c] = [floor(index / 9), floor(index % 9)];

    // 是否找到解决方案？
    if (index === 9 * 9) {
      halt = true;
      return;
    }

    // 剪枝：如果当前位置不是空的，从下一个位置开始
    if (board[r][c] !== '.') {
      index++;
      backtrack();
      index--;
      return;
    }

    for (let val = 1; val <= 9; val++) {
      // 剪枝：如果当前值不合法，跳过
      if (!isValid(r, c, val)) continue;

      // 更新状态
      index++;
      board[r][c] = String(val);

      // 做选择
      backtrack();

      // 只需要找到一个解决方案
      if (halt) return;

      // 撤销状态
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
    console.log(row.join(' '));
  }
}
