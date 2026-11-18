class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(1, n, 2):
            if s[i - 1] != s[i]:
                ans += 1
        return ans
