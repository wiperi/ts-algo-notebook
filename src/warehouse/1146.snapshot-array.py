#
# @lc app=leetcode.cn id=1146 lang=python3
# @lcpr version=30204
#
# [1146] 快照数组
#


# @lcpr-template-start
import bisect
from collections import defaultdict
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start



class SnapshotArray:

    def __init__(self, length: int):
        self.mp = defaultdict(list)
        self.id = 0

    def set(self, index: int, val: int) -> None:
        self.mp[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        ls = self.mp[index]
        ind = bisect.bisect_right(ls, snap_id, key=lambda a:a[0]) - 1
        return ls[ind][1] if ind >= 0 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

#
# @lcpr case=start
# ["SnapshotArray","set","snap","set","get"][[3],[0,5],[],[0,6],[0,0]]\n
# @lcpr case=end

#

