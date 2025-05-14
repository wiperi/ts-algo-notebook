#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#


# @lcpr-template-start
from collections import defaultdict
from ctypes import oledll
from time import sleep
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start

class Node:
    def __init__(self, key = 0, val = 0) -> None:
        self.key = key
        self.val = val
        self.next: Node = None
        self.prev: Node = None

class Dlist:
    # head to be newest

    def __init__(self) -> None:
        left = Node()
        right = Node()

        left.next = right
        right.prev = left

        self.right = right
        self.left = left

    def delete(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None
        return node

    def moveToHead(self, node: Node):
        deleted = self.delete(node)        
        self.addToHead(deleted)

    def addToHead(self, node: Node):
        head = self.left.next
        self.left.next = node
        head.prev = node

        node.prev = self.left
        node.next = head


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ls = Dlist()
        self.mp: dict[int, Node] = defaultdict(lambda : -1)
        

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.ls.moveToHead(node)
            return node.val
        elif key not in self.mp:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.ls.moveToHead(node)
        elif key not in self.mp:
            if len(self.mp) == self.capacity:
                oldest = self.ls.right.prev
                del self.mp[oldest.key]
                self.ls.delete(oldest)

            # not full
            node = Node(key, value)
            self.mp[key] = node
            self.ls.addToHead(node)

        
cache = LRUCache(2)

cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
print(cache.get(1))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



