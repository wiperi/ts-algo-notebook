/*
 * @lc app=leetcode.cn id=79 lang=typescript
 *
 * [79] 单词搜索
 */

// @lc code=start
function exist(board: string[][], word: string): boolean {
  let found = false;
  let row = board.length;
  let col = board[0].length;

  function cor(index: number): [number, number] {
    return [Math.floor(index / col), index % col];
  }

  let used = Array(row * col).fill(false);

  for (let i = 0; i < row * col; i++) {
    backtrack(i, 0);
    if (found) break;
  }

  return found;

  /***
   * @param index 二位数组的一维索引，当前遍历的位置
   * @param pos 正在匹配的字符在 word 中的索引
   */
  function backtrack(index: number, pos: number) {
    used[index] = true;

    let [r, c] = cor(index);
    if (board[r][c] !== word[pos]) {
      used[index] = false;
      return;
    }

    if (pos === word.length - 1) {
      found = true;
      return;
    }

    for (let shift of [col, -1, 1, -col]) {
      let newIndex = index + shift;
      let [newR, newC] = cor(newIndex);

      // 边界检查
      if (newIndex < 0 || newIndex >= row * col) continue;
      // 检查曼哈顿距离是否为1，ie. 只允许上下左右移动
      if (Math.abs(r - newR) + Math.abs(c - newC) !== 1) continue;
      // 防止死循环
      if (used[newIndex]) continue;

      backtrack(newIndex, pos + 1);
      if (found) return;
    }

    used[index] = false;
  }
}
// @lc code=end
if (require.main === module) {
  exist(
    [
      ['A', 'B', 'C', 'E'],
      ['S', 'F', 'C', 'S'],
      ['A', 'D', 'E', 'E'],
    ],
    'ABCCED'
  );
}

export {}