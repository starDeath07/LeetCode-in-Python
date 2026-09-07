class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1

        prev = ord("a")
        start = 0

        for i in range(n):
            if prev + 1 != ord(s[i]):
                start = i
            ans = max(ans, i - start + 1)
            prev = ord(s[i])

        return ans
