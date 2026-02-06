class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = right = 0
        max_size = 0
        while right < n:
            while nums[right] > nums[left] * k:
                left += 1
            max_size = max(max_size, right - left + 1)
            right += 1
        return n - max_size
