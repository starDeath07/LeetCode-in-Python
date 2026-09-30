class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans: list[int] = []

        for c in seq:
            if c == "(":
                depth += 1
                ans.append(0 if depth % 2 == 0 else 1)
            else:
                ans.append(0 if depth % 2 == 0 else 1)
                depth -= 1

        return ans
