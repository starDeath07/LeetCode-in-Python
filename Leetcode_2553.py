class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans: list[int] = [int(i) for num in nums for i in str(num)]
        return ans
