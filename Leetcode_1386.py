class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        m = len(reservedSeats)
        ans = n * 2

        reservedSeats.sort()

        j = 0
        used: list[bool] = [False] * (11)

        while j < m:
            k = j
            while k < m and reservedSeats[k][0] == reservedSeats[j][0]:
                used[reservedSeats[k][1]] = True
                k += 1

            check2_5 = self.check_for2to5(used, 2, 5)
            check4_7 = self.check_for4to7(used, 4, 7)
            check6_9 = self.check_for6to9(used, 6, 9)

            if check2_5 and check6_9:
                pass
            elif check2_5 or check4_7 or check6_9:
                ans -= 1
            else:
                ans -= 2

            used = [False] * (11)
            j = k

        return ans

    def check_for2to5(self, used: list[bool], l: int, r: int) -> bool:
        for i in range(l, r + 1):
            if used[i]:
                return False

        return True

    def check_for4to7(self, used: list[bool], l: int, r: int) -> bool:
        for i in range(l, r + 1):
            if used[i]:
                return False

        return True

    def check_for6to9(self, used: list[bool], l: int, r: int) -> bool:
        for i in range(l, r + 1):
            if used[i]:
                return False

        return True
