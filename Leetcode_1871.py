class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == "1":
            return False
        dp = [0] * n
        count = 0

        for i in range(n):
            count += dp[i]

            if i == 0 or (s[i] == "0" and count > 0):
                if i + minJump < n:
                    dp[i + minJump] += 1
                if i + maxJump + 1 < n:
                    dp[i + maxJump + 1] -= 1

        return count > 0
