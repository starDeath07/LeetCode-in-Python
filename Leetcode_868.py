class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        prev = -1

        for i in range(32):
            curr = n & 1
            if curr == 1 and prev != -1:
                ans = max(ans, i - prev)
            if curr == 1:
                prev = i
            n >>= 1
        return ans
