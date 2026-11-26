class Solution:
    def canAliceWin(self, n: int) -> bool:
        diff = 10

        while n >= 0:
            n -= diff
            if n < 0:
                return diff % 2 != 0
            diff -= 1

        return False
