#
# @lc app=leetcode.cn id=785 lang=python3
# @lcpr version=30204
#
# [785] 判断二分图
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        vis = [False] * n
        part = [1] * n

        for start in range(n):
            if vis[start]:
                continue

            q = [start]
            vis[start] = True

            while q:
                levelSize = len(q)

                for _ in range(levelSize):
                    node = q.pop(0)

                    for ch in graph[node]:
                        if vis[ch]:
                            if part[ch] == part[node]:
                                return False
                            continue

                        part[ch] = part[node] * -1
                        vis[ch] = True
                        q.append(ch)

        return True


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[0,2],[0,1,3],[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[0,2],[1,3],[0,2]]\n
# @lcpr case=end

#
