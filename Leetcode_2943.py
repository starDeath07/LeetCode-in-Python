from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()
        side: int = min(self.finder(hBars), self.finder(vBars)) + 1
        return side * side

    def finder(self, arr: List[int]):
        curr = 1
        res = 1

        for i in range(1, len(arr)):
            if arr[i - 1] + 1 == arr[i]:
                curr += 1
            else:
                curr = 1
            res = max(res, curr)
        return res
