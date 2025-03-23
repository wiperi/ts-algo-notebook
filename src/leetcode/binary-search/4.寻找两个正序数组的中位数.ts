/*
 * @lc app=leetcode.cn id=4 lang=typescript
 * @lcpr version=30104
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {

  // Idea:
  // The median is the the Kth smallest value in the array, where k = len(arr) / 2.
  // So, we only to find the Kth smallest value.

  // O(m + n)

  let totalLength = nums1.length + nums2.length;

  let middleIndex = Math.floor(totalLength / 2);

  // Determin howm any value is the middle value
  let twoMiddle = false;
  if (totalLength % 2 === 0) {
    twoMiddle = true;
  }

  // First middle value and second middle value.
  // If totalLength is odd, then we only need second value.
  let first;
  let second;

  let i = 0;
  let j = 0;
  let index = 0;
  while (1) {
    let current;

    if (i < nums1.length && j < nums2.length) {
      if (nums1[i] < nums2[j]) {
        current = nums1[i++];
      } else {
        current = nums2[j++];
      }
    } else if (i == nums1.length && j < nums2.length) {
      // Nums1 is exausted
      current = nums2[j++];
    } else if (i < nums1.length && j == nums2.length) {
      // Nums2 is exausted
      current = nums1[i++];
    }
    // console.log(current);

    if (index === middleIndex - 1) {
      first = current;
    }
    if (index === middleIndex) {
      second = current;
      break;
    }

    index++;
  }

  if (twoMiddle) {
    return (first + second) / 2;
  } else {
    return second;
  }
}
// @lc code=end

/*
// @lcpr case=start
// [1,3]\n[2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n[3,4]\n
// @lcpr case=end

 */
