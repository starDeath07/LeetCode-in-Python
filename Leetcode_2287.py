from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq: Counter[str] = Counter(s)
        target_freq: Counter[str] = Counter(target)
        ans = 10**10
        for c in target:
            ans = min(ans, freq[c] // target_freq[c])
        return ans
