class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        sweep_line = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            # assume all the sum takes 2 moves between the range
            sweep_line[2] += 2
            sweep_line[2 * limit + 1] -= 2

            # takes 1 move if the it lies between min + 1 and max + limit + 1
            sweep_line[a + 1] -= 1
            sweep_line[b + limit + 1] += 1

            # 0 move if the sum is target
            sweep_line[a + b] -= 1
            sweep_line[a + b + 1] += 1

        return min(accumulate(sweep_line[2 : 2 * limit + 1]))
