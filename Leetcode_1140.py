from functools import cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        INF = 10**18
        n = len(piles)

        @cache
        def finder(index: int, person: bool, M: int) -> int:
            if index >= n:
                return 0

            stones = 0
            result = 0 if person else INF

            for i in range(1, min(2 * M, n - index) + 1):
                stones += piles[index + i - 1]
                if person:
                    result = max(result, stones + finder(index + i, False, max(i, M)))
                else:
                    result = min(result, finder(index + i, True, max(i, M)))
            return result

        return finder(0, 1, True)
