from functools import cache


class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        @cache
        def finder(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            l = nums[left] - finder(left + 1, right)
            r = nums[right] - finder(left, right - 1)

            return max(l, r)

        return finder(0, len(nums) - 1) >= 0
