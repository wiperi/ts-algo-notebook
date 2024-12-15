/*
 * @lc app=leetcode id=51 lang=typescript
 *
 * [51] N-Queens
 */

// @lc code=start
function solveNQueens(n: number): string[][] {
    
    const board = Array(n).fill(0).map(() => Array(n).fill('.'));
    let res = [];

    backtrack(0);

    return res;


    function backtrack(r) {
        
        if (r === 4) {
            res.push(JSON.parse(JSON.stringify(board)));
            return;
        }

        for (let c = 0; c < 4; c++) {

            if (!isValid(r, c)) continue;

            board[r][c] = 'Q';
            backtrack(r + 1);
            board[r][c] = '.';
        }
    }

    function isValid(r, c) {
        for (let i = 0; i < n; i++) {
            if (board[i][c] === 'Q') return false;
            if (board[r][i] === 'Q') return false;

            for (let j = 0; j < n; j++) {
                if (i + j === r + c && board[i][j] === 'Q') return false;
                if (i - j === r - c && board[i][j] === 'Q') return false;
            }
        }

        return true;
    }
};

if (require.main === module) {
    let res = solveNQueens(4);

    for (const row of res) {
        console.log(row.join(' '));
    }


}
// @lc code=end

