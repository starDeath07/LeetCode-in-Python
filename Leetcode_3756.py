class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        MOD = 10**9 + 7

        power = [0] * (n + 1)
        total = [0] * (n + 1)
        number_formed = [0] * (n + 1)
        non_zero = [0] * (n + 1)

        power[0] = 1

        for i in range(1, n + 1):
            digit: int = ord(s[i - 1]) - ord("0")
            power[i] = (power[i - 1] * 10) % MOD
            total[i] = total[i - 1] + digit

            if digit:
                number_formed[i] = (number_formed[i - 1] * 10 + digit) % MOD
                non_zero[i] = non_zero[i - 1] + 1
            else:
                number_formed[i] = number_formed[i - 1]
                non_zero[i] = non_zero[i - 1]

        ans: list[int] = []

        for left, right in queries:
            tot = total[right + 1] - total[left]
            k = non_zero[right + 1] - non_zero[left]
            x = (
                number_formed[right + 1] - (number_formed[left] * power[k]) % MOD + MOD
            ) % MOD
            val = (x * tot) % MOD
            ans.append(val)

        return ans
