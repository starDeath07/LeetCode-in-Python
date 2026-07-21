class Solution:
    def maxActiveSessionsAfterTrade(self, s: str) -> int:
        zero: list[int] = []
        n = len(s)
        one = 0
        maxi = 0

        start = 0

        while start < n:
            if s[start] == "1":
                one += 1
                start += 1
                continue

            if s[start] == "0":
                j = start

                while j < n and s[j] == "0":
                    j += 1
                zero.append(j - start)
                start = j

        for i in range(1, len(zero)):
            maxi = max(maxi, zero[i - 1] + zero[i])

        return maxi + one
