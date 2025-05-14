/*
 * @lc app=leetcode.cn id=6 lang=typescript
 * @lcpr version=30104
 *
 * [6] Z 字形变换
 */

// @lc code=start
function convert(s: string, numRows: number): string {
  if (numRows < 2) {
    return s;
  }

  let res = Array.from({ length: numRows }, v => '');

  // Which row that char should be appended to
  let rowIndex = 0;
  // Flag that determine which direciton we are going on the Z shape, going up or going down
  let goingDown = true;

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    // Append char to the correct row
    res[rowIndex] += char;

    // Update row
    if (goingDown) {
      rowIndex++;
    } else {
      rowIndex--;
    }

    // Change to reversed direciton when reached a boundary
    if (rowIndex === numRows - 1 || rowIndex === 0) {
      goingDown = !goingDown;
    }
  }

  return res.join('');
}
// @lc code=end

/*
// @lcpr case=start
// "PAYPALISHIRING"\n3\n
// @lcpr case=end

// @lcpr case=start
// "PAYPALISHIRING"\n4\n
// @lcpr case=end

// @lcpr case=start
// "A"\n1\n
// @lcpr case=end

 */
