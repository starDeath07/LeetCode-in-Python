class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        ans = 0

        for pattern in patterns:
            if pattern in word:
                ans += 1
        return ans
