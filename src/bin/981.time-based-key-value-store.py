#
# @lc app=leetcode.cn id=981 lang=python3
# @lcpr version=30204
#
# [981] 基于时间的键值存储
#


# @lcpr-template-start
import bisect
from collections import defaultdict
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        ls = self.mp[key]
        ind = bisect.bisect_right(ls, timestamp, key=lambda a: a[0])
        
        if ind == 0:
            return ''
        else:
            return ls[ind -1][1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end



#
# @lcpr case=start
# ["TimeMap", "set", "get", "get", "set", "get", "get"][[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]\n
# @lcpr case=end

#

