class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        ans = 0
        carry = 0

        for i in range(n - 1, 0, -1):
            if ord(s[i]) - ord("0") + carry == 1:
                ans += 2
                carry = 1
            else:
                ans += 1
        return ans + carry
