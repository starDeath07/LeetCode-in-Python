class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        multiples = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            cnt = 0
            for m in range(g, mx + 1, g):
                cnt += freq[m]
            multiples[g] = cnt

        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            total = multiples[g] * (multiples[g] - 1) // 2
            for m in range(2 * g, mx + 1, g):
                total -= exact[m]
            exact[g] = total

        pref = [0] * (mx + 1)
        for g in range(1, mx + 1):
            pref[g] = pref[g - 1] + exact[g]

        ans: list[int] = []
        for q in queries:
            k = q + 1
            lo, hi = 1, mx
            while lo < hi:
                mid = (lo + hi) // 2
                if pref[mid] >= k:
                    hi = mid
                else:
                    lo = mid + 1
            ans.append(lo)

        return ans
