class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)
        arr.sort()
        arr[0] = 1

        for i in range(1, n):
            arr[i] = min(arr[i - 1] + 1, arr[i])
        return arr[n - 1]
