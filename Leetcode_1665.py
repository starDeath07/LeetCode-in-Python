class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        minn = 0
        maxx = 0
        ans = 0
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        for actual, minimum in tasks:
            minn = max(minn, minimum)
            maxx += minimum

        while minn <= maxx:
            mid = minn + (maxx - minn) // 2
            if self.valid(tasks, mid):
                ans = mid
                maxx = mid - 1
            else:
                minn = mid + 1

        return ans

    def valid(self, tasks: list[list[int]], t: int) -> bool:
        power = t

        for actual, minimum in tasks:
            if power < minimum:
                return False
            power -= actual

        return True

