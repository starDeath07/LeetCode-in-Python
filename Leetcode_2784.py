class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        arr: list[int] = [0] * n

        for num in nums:
            if num >= n:
                return False
            arr[num] += 1
            if arr[num] > 1 and num != n - 1:
                return False

        return arr[-1] == 2
