class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        res = 30 * (hour + minutes / 60) - 6 * minutes
        res = abs(res)
        return res if res < 180.0 else 360.0 - res
