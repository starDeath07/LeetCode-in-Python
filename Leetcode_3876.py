class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = 0
        mini = 10**10

        for num in nums1:
            mini = min(mini, num)
            if num % 2 == 1:
                odd += 1

        return odd == 0 or mini % 2 == 1
