class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def dp(nums: list[int]) -> int:
            n = len(nums)
            if n < 3:
                return 1
            root: int = nums[0]
            left: list[int] = []
            right: list[int] = []

            for x in nums:
                if x < root:
                    left.append(x)
                elif x > root:
                    right.append(x)

            return dp(left) * dp(right) * comb(n - 1, len(left))

        return (dp(nums) - 1) % 1000000007
