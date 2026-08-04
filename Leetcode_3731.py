class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        start = 10**10
        end = 0
        seen: set[int] = set()

        for num in nums:
            start = min(start, num)
            end = max(end, num)
            seen.add(num)

        ans: list[int] = []
        while start < end:
            if start not in seen:
                ans.append(start)
            start += 1

        return ans
