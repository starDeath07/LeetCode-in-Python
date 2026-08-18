class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subarray_count: dict[int, int] = {}

        for i in range(n - k + 1):
            for num in set(nums[i : i + k]):
                subarray_count[num] = subarray_count.get(num, 0) + 1

        ans = -1
        for num, count in subarray_count.items():
            print(num, count)
            if count == 1 and num > ans:
                ans = num

        return ans
