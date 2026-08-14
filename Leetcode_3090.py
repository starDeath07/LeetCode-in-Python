from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        freq: defaultdict[str, int] = defaultdict(int)
        ans = 0
        start = 0
        end = 0

        while end < n:
            freq[s[end]] += 1
            while freq[s[end]] > 2:
                freq[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
            end += 1

        return ans
