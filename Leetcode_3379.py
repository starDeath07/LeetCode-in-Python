class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res: list[int] = []
        for i in range(n):
            index = ((i + nums[i] % n) + n) % n
            res.append(nums[index])
        return res
