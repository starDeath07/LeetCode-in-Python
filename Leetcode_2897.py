class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bin: list[int] = [0] * 31

        for num in nums:
            for i in range(31):
                if num & (1 << i):
                    bin[i] += 1

        ans = 0

        for _ in range(k):
            x = 0
            for i in range(31):
                if bin[i] > 0:
                    x |= 1 << i
                    bin[i] -= 1
            ans = (ans + x * x) % MOD

        return ans
