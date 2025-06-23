/*
 * @lc app=leetcode.cn id=283 lang=java
 * @lcpr version=30204
 *
 * [283] 移动零
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.LinkedList;
import java.util.SortedSet;

class Solution {
    public void moveZeroes(int[] nums) {
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                swap(nums, i, start++);
            }
        }
    }

    void swap(int[] nums, int i,int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [0,1,0,3,12]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n
// @lcpr case=end

 */

