import math


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        left = 1
        right = max(workerTimes) * (mountainHeight * (mountainHeight + 1) // 2)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            if self.valid(mountainHeight, workerTimes, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def valid(self, height: int, times: list[int], mid: int) -> bool:
        curr = 0

        for time in times:
            curr += int((-1 + math.sqrt(1 + 8 * mid // time)) // 2)
            if curr >= height:
                return True

        return False
