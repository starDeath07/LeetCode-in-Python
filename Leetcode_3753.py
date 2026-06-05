from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return self._func(num2) - self._func(num1 - 1)

    def _func(self, n: int) -> int:
        if n < 100:
            return 0

        num = str(n)

        @lru_cache(None)
        def dfs(
            index: int, tight: bool, left: int, mid: int, lead_zero: bool
        ) -> tuple[int, int]:
            if index == len(num):
                return (1, 0)  # (count, waviness)

            limit = int(num[index]) if tight else 9

            total_count = 0
            total_wave = 0

            for right in range(limit + 1):
                new_tight = tight and (right == limit)
                new_lead_zero = lead_zero and (right == 0)

                new_left = mid
                new_mid = -1 if new_lead_zero else right

                count, wave = dfs(
                    index + 1, new_tight, new_left, new_mid, new_lead_zero
                )

                if (not lead_zero) and left >= 0 and mid >= 0:
                    if mid > max(left, right) or mid < min(left, right):
                        total_wave += count

                total_count += count
                total_wave += wave

            return (total_count, total_wave)

        return dfs(0, True, -1, -1, True)[1]
