class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        mini = 10**10
        maxi = -(10**10)
        pos1 = -1
        pos2 = -1

        for i in range(n):
            if nums[i] < mini:
                mini = nums[i]
                pos1 = i
            if nums[i] > maxi:
                maxi = nums[i]
                pos2 = i

        return min(
            max(pos1, pos2) + 1,
            n - min(pos1, pos2),
            min(pos1, pos2) + 1 + n - max(pos1, pos2),
        )
