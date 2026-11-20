class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        gcd = numsDivide[0]

        def gcd_finder(a: int, b: int) -> int:
            if b == 0:
                return a
            x = gcd_finder(b, a % b)
            return x

        for num in set(numsDivide):
            gcd = gcd_finder(gcd, num)

        for i, num in enumerate(sorted(nums)):
            if gcd % num == 0:
                return i

        return -1
