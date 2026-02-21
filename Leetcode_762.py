class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        primes = {2, 3, 5, 7, 11, 17, 13, 19, 23, 29}
        while left <= right:
            if bin(left).count("1") in primes:
                ans += 1
            left += 1
        return ans
