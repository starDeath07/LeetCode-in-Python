from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        n = len(nums)
        INF = 10**18
        ans = INF
        total = 0
        lesser: SortedList[int] = SortedList(key=lambda i: (nums[i], i))
        greater: SortedList[int] = SortedList(key=lambda i: (nums[i], i))

        for i in range(1, dist + 2):
            total += nums[i]
            lesser.add(i)

        while len(lesser) > k - 1:
            index = lesser.pop()
            total -= nums[index]
            greater.add(index)

        ans = min(ans, total)

        for i in range(1, n - dist - 1):
            index = i + dist + 1
            greater.add(index)

            if i in lesser:
                total -= nums[i]
                lesser.remove(i)

                curr_index = greater.pop(0)
                total += nums[curr_index]
                lesser.add(curr_index)
            else:
                greater.remove(i)

                a = lesser[-1]
                b = greater[0]

                if nums[b] < nums[a]:
                    total -= nums[a]
                    total += nums[b]

                    lesser.remove(a)
                    lesser.add(b)

                    greater.remove(b)
                    greater.add(a)

            ans = min(ans, total)

        return ans + nums[0]
