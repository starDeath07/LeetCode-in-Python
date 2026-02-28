class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9 + 7

        for i in range(n + 1):
            curr = i
            size = 0
            while curr:
                curr >>= 1
                size += 1
            ans <<= size
            ans += i
            ans %= MOD

        return ans % MOD

    # another way to do this directly by getting the length of decimal in binary form
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9 + 7

        for i in range(n + 1):
            ans = (ans << i.bit_length()) + i
            ans %= MOD

        return ans
