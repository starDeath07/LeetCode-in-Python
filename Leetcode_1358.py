from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        freq: defaultdict[str, int] = defaultdict(int)

        start = 0

        for end in range(n):
            freq[s[end]] += 1

            while len(freq) == 3 and start < end:
                ans += n - end
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    freq.pop(s[start])
                start += 1

        return ans
