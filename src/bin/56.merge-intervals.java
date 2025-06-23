/*
 * @lc app=leetcode.cn id=56 lang=java
 * @lcpr version=30204
 *
 * [56] 合并区间
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        var res = new ArrayList<int[]>();
        int i = 0;
        while (i < intervals.length) {
            int[] curr = intervals[i];

            int j = i + 1;
            while (j < intervals.length && intervals[j][0] <= curr[1]) {
                curr[1] = Math.max(curr[1], intervals[j][1]);
                j += 1;
            }
            i = j;

            res.add(curr);
        }

        return res.toArray(new int[][] {});
    }
}
// @lc code=end



/*
// @lcpr case=start
// [[1,3],[2,6],[8,10],[15,18]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,4],[4,5]]\n
// @lcpr case=end

 */

