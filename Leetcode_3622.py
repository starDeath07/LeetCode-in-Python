class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        prod = 1
        temp = n

        while temp:
            rem = temp % 10
            temp //= 10
            total += rem
            prod *= rem

        return n % (total + prod) == 0
