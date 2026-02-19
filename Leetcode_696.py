class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        prev = 0
        curr = 1

        for i in range(1, n):
            if s[i - 1] == s[i]:
                curr += 1
            else:
                prev = curr
                curr = 1

            if prev >= curr:
                ans += 1
        return ans
