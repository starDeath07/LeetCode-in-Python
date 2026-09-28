class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        curr = 0
        ans = 0

        for i in range(n):
            if s[i] == "(":
                curr += 1
            elif s[i] == ")":
                ans = max(curr, ans)
                curr -= 1

        return ans
