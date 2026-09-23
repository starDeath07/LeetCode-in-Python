class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        remaining = total - x

        if remaining < 0:
            return -1
        if remaining == 0:
            return n

        left = 0
        right = 0
        ans = -1
        curr = 0

        while right < n:
            curr += nums[right]

            while left <= right and curr > remaining:
                curr -= nums[left]
                left += 1

            if curr == remaining:
                ans = max(ans, right - left + 1)

            right += 1

        return -1 if ans == -1 else n - ans
