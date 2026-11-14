class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        ans = 10**18
        prefix = [0]

        for i in range(n):
            prefix.append(prefix[-1] + nums[i])

        for j in range(l, n + 1):
            for length in range(l, min(r, j) + 1):
                total = prefix[j] - prefix[j - length]
                if 0 < total < ans:
                    ans = total

        return -1 if ans == 10**18 else ans
