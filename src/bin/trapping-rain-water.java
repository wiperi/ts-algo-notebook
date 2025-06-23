/*
 * @lc app=leetcode.cn id=42 lang=java
 * @lcpr version=30204
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        var left = new int[height.length];
        var right = new int[height.length];

        int max = 0;
        for (int i = 0;i < height.length; i++) {
            max = Math.max(max, height[i]);
            left[i] = max;
        }

        max = 0;
        for (int i = height.length - 1; i >= 0; i--) {
            max = Math.max(max, height[i]);
            right[i] = max;
        }

        int total_water = 0;
        for (int i = 0; i < height.length; i++) {
            total_water += Math.min(left[i], right[i]) - height[i];
        }

        return total_water;

    }
}
// @lc code=end



/*
// @lcpr case=start
// [0,1,0,2,1,0,1,3,2,1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [4,2,0,3,2,5]\n
// @lcpr case=end

 */

