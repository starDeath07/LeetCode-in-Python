from collections import defaultdict


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        rh = RollingHash(nums)
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            map: defaultdict[int, int] = defaultdict(int)

            for i in range(n - mid + 1):
                curr = rh.getHash(i, i + mid - 1)
                map[curr] += 1

            found = False
            for val in map.values():
                if val == 1:
                    found = True
                    break

            if found:
                right = mid - 1
            else:
                left = mid + 1

        return left


class RollingHash:
    BASE: int = 31
    MOD: int = 10**9 + 7

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.power: list[int] = [1]
        self.hash: list[int] = [0]
        self.__buildHash()

    def __buildHash(self) -> None:
        for i in range(len(self.nums)):
            self.hash.append((self.hash[-1] * self.BASE + self.nums[i]) % self.MOD)
            self.power.append((self.power[-1] * self.BASE) % self.MOD)

    def getHash(self, left: int, right: int) -> int:
        return (
            self.hash[right + 1]
            - self.hash[left] * self.power[right - left + 1] % self.MOD
            + self.MOD
        ) % self.MOD
