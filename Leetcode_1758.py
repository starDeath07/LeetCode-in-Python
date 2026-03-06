class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            if ord(s[i]) - ord("0") != i % 2:
                ans += 1

        return min(ans, n - ans)

