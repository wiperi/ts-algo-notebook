/*
 * @lc app=leetcode.cn id=11 lang=java
 * @lcpr version=30204
 *
 * [11] 盛最多水的容器
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        // water = right - left * min(left, right)
        int l = 0;
        int r = height.length - 1;
        int maxWater = 0;

        while (l < r) {
            int water = (r - l) * Math.min(height[l], height[r]);
            maxWater = Math.max(maxWater, water);

            if (height[l] < height[r]) {
                l += 1;
            } else {
                r -= 1;
            }
        }

        return maxWater;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,8,6,2,5,4,8,3,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,1]\n
// @lcpr case=end

 */

