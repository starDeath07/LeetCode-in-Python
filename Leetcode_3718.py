class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        seen: set[int] = set(nums)
        temp = k

        while temp in seen:
            temp += k

        return temp
