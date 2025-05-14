#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30104
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start


class Trie:

    def __init__(self):
        self.children: list[Trie] = [None] * 26 # type: ignore
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ind = ord(ch) - ord("a")

            if node.children[ind] is None:
                node.children[ind] = Trie()

            node = node.children[ind]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            i = ord(ch) - ord("a")

            if node.children[i] is None:
                return False

            node = node.children[i]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            i = ord(ch) - ord("a")

            if node.children[i] is None:
                return False

            node = node.children[i]

        return True

# @lc code=end

res = Trie().insert("abc")

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
