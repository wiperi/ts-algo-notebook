#
# @lc app=leetcode.cn id=744 lang=python3
# @lcpr version=30204
#
# [744] 寻找比目标字母大的最小字母
#


# @lcpr-template-start
from bisect import bisect_right
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect_right(letters, target) % len(letters)
        return letters[i]
# @lc code=end



#
# @lcpr case=start
# ["c", "f"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# ["c","f","j"]\n"c"\n
# @lcpr case=end

# @lcpr case=start
# ["x","x","y","y"]\n"z"\n
# @lcpr case=end

#

