/*
 * @lc app=leetcode.cn id=84 lang=java
 * @lcpr version=30204
 *
 * [84] 柱状图中最大的矩形
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.Arrays;
import java.util.Stack;

class Solution {
    public int largestRectangleArea(int[] heights) {
        // area = (r - l) * height[i]

        int[] leftSmall = new int[heights.length];
        int[] rightSmall = new int[heights.length];

        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < heights.length; i++) {
            while (!st.isEmpty() && heights[i] <= heights[st.peek()]) {
                st.pop();
            }
            if (!st.isEmpty()) {
                leftSmall[i] = st.peek();
            } else {
                leftSmall[i] = -1;
            }
            st.add(i);
        }

        st.clear();
        for (int i = heights.length - 1; i >= 0; i--) {
            while (!st.isEmpty() && heights[i] <= heights[st.peek()]) {
                st.pop();
            }
            if (!st.isEmpty()) {
                rightSmall[i] = st.peek();
            } else {
                rightSmall[i] = heights.length;
            }
            st.add(i);
        }

        // Arrays.stream(leftSmall).forEach(System.out::println);
        // System.out.println();
        // Arrays.stream(rightSmall).forEach(System.out::println);

        int res = 0;
        for (int i = 0; i < heights.length; i ++) {
            int area = (rightSmall[i] - leftSmall[i] - 1) * heights[i];
            res = Math.max(res, area);
        }

        return res;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [2,1,5,6,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [2,4]\n
// @lcpr case=end

 */

