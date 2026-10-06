class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        count = 0
        pairs = 0

        for i in range(n):
            if s[i] == "(":
                count += 1
            elif count:
                count -= 1
                pairs += 2

        return n - pairs
