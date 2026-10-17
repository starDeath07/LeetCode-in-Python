class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        arr: list[tuple[int, int, int]] = []

        for i, num in enumerate(nums):
            digit_sum = sum(int(d) for d in str(num))
            arr.append((digit_sum, num, i))

        arr.sort()

        ans = 0
        i = 0

        while i < n:
            if arr[i][2] == i:
                i += 1
            else:
                index = arr[i][2]
                arr[i], arr[index] = arr[index], arr[i]
                ans += 1

        return ans
