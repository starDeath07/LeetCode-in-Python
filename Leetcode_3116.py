import math


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        self.n = len(coins)
        self.m = 1 << self.n

        left = k
        right = min(coins) * k + 1
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if self.get_correct_count(coins, mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

    def get_correct_count(self, coins: list[int], mid: int) -> int:
        count: int = 0

        for i in range(1, self.m):
            order = 0
            lcm: int = 1

            for j in range(self.n):
                if i & (1 << j):
                    order += 1
                    lcm = math.lcm(lcm, coins[j])

            if order % 2:
                count += mid // lcm
            else:
                count -= mid // lcm

        return count
