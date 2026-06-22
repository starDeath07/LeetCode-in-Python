from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq: Counter[str] = Counter(text)
        ans = 10**10

        for c in "aboln":
            if c in "ol":
                ans = min(ans, freq[c] // 2)
            ans = min(ans, freq[c])
        return ans
