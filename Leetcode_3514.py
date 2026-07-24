class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        SIZE = 2048
        n = len(nums)
        pair: list[int] = [0] * SIZE
        triple: list[int] = [0] * SIZE

        for i in range(n):
            for j in range(i, n):
                pair[nums[i] ^ nums[j]] = 1

        for i in range(SIZE):
            if pair[i]:
                for j in range(n):
                    triple[i ^ nums[j]] = 1

        ans = 0

        for i in range(SIZE):
            if triple[i] == 1:
                ans += 1

        return ans
