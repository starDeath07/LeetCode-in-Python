class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)
        ans: list[list[int]] = []
        small = 10**10

        arr.sort()
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]

            if diff < small:
                small = diff
                ans.clear()
                ans.append([arr[i - 1], arr[i]])
            elif diff == small:
                ans.append([arr[i - 1], arr[i]])

        return ans
