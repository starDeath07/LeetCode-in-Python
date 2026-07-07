class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        x = 0
        mult = 1

        while n:
            rem = n % 10
            n //= 10

            if rem:
                total += rem
                x = mult * rem + x
                mult *= 10

        return x * total
