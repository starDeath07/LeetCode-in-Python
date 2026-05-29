class Solution:
    def minElement(self, nums: list[int]) -> int:
        ans = 10**18
        for num in nums:
            curr = 0
            while num > 0:
                curr += num % 10
                num //= 10
            ans = min(ans, curr)
        return ans
