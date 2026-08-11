class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        seen: set[int] = set(nums)
        total = nums[0]

        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                total += nums[i]
            else:
                break

        while total in seen:
            total += 1

        return total
