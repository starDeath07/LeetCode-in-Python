from collections import defaultdict


class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        mp: defaultdict[int, int] = defaultdict(int)
        ans = 0

        for num in nums:
            val1 = mp[num] + 1
            val2 = mp[num - 1] + 1

            next = max(mp[num + 1], val1)
            curr = max(mp[num - 1], val2)

            ans = max(ans, curr, next)
            mp[num] = curr
            mp[num + 1] = next

        return ans
