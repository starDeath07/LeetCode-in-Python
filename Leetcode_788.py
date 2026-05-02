class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0

        for i in range(n + 1):
            num = i
            valid = True
            update = False

            while num > 0:
                digit = num % 10
                if digit in (2, 5, 6, 9):
                    update = True
                if digit in (3, 4, 7):
                    valid = False
                num //= 10

            if valid and update:
                ans += 1

        return ans
