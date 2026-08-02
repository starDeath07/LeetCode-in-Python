from functools import cache


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @cache
        def finder(left: int, right: int) -> int:
            if left == right:
                return piles[left]
            l = piles[left] - finder(left + 1, right)
            r = piles[right] - finder(left, right - 1)
            return max(l, r)

        return finder(0, len(piles) - 1) > 0
