class Trie:
    class Node:
        def __init__(self) -> None:
            self.children: dict[str, "Trie.Node"] = {}
            self.is_end: bool = False

    def __init__(self) -> None:
        self.root: Trie.Node = self.Node()

    def insert(self, s: str) -> None:
        curr: Trie.Node = self.root

        for ch in s:
            if ch not in curr.children:
                curr.children[ch] = self.Node()

            curr = curr.children[ch]

        curr.is_end = True

    def find_prefix(self, s: str) -> int:
        curr: Trie.Node = self.root
        count: int = 0

        for ch in s:
            if ch not in curr.children:
                return count

            curr = curr.children[ch]
            count += 1

        return count


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie: Trie = Trie()
        ans: int = 0

        for val in arr1:
            trie.insert(str(val))

        for val in arr2:
            ans = max(ans, trie.find_prefix(str(val)))

        return ans
