class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        mapping: list[list[int]] = [[], [], []]

        for num in nums:
            mapping[num % 3].append(num)

        ans = 0
        if len(mapping[0]) > 2:
            ans = max(ans, sum(mapping[0][:3]))

        if len(mapping[0]) > 0 and len(mapping[1]) > 0 and len(mapping[2]) > 0:
            ans = max(ans, mapping[0][0] + mapping[1][0] + mapping[2][0])

        if len(mapping[1]) > 2:
            ans = max(ans, sum(mapping[1][:3]))

        if len(mapping[2]) > 2:
            ans = max(ans, sum(mapping[2][:3]))

        return ans
