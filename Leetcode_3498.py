class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            ans += (26 - ord(s[i]) + ord("a")) * (i + 1)

        return ans
