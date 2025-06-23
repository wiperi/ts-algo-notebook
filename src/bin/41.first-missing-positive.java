/*
 * @lc app=leetcode.cn id=41 lang=java
 * @lcpr version=30204
 *
 * [41] 缺失的第一个正数
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
class Solution {
    public int firstMissingPositive(int[] nums) {
        
        for (int i = 0; i < nums.length; i++) {
            while ((nums[i] - 1) >= 0 && (nums[i] - 1) < nums.length && nums[nums[i] - 1] != nums[i]) {
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (i + 1 != nums[i]) {
                return i + 1;
            }
        }
        
        return nums.length + 1;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,0]\n
// @lcpr case=end

// @lcpr case=start
// [3,4,-1,1]\n
// @lcpr case=end

// @lcpr case=start
// [7,8,9,11,12]\n
// @lcpr case=end

 */

