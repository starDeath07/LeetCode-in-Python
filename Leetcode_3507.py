class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        INF = 10**10

        while True:
            min_sum = INF
            pos = -1
            flag = True
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    flag = False

                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    pos = i

            if flag:
                return ans
            nums[pos] = min_sum

            for i in range(pos + 1, n - 1):
                nums[i] = nums[i + 1]
            n -= 1
            ans += 1
