class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans: list[int] = []
        for i, num in enumerate(sorted(nums)):
            if num == target:
                ans.append(i)

        return ans
