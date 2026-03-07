class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ans = 10**10
        index, diff1, diff2 = 0, 0, 0

        for i in range(2 * n):
            val = ord(s[i % n]) - ord("0")

            if i % 2 != val:
                diff1 += diff1

            if (i + 1) % 2 != val:
                diff2 += 1

            if i >= n:
                if index % 2 != val:
                    diff1 -= 1
                if (index + 1) % 2 != val:
                    diff2 -= 1
                index += 1

                ans = min(ans, diff1, diff2)
        return ans
