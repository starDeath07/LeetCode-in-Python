import heapq
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        ans: list[int] = []
        freq: list[int] = [0] * k

        inc_list: SortedList[int] = SortedList(i for i in range(k))
        used = []

        max_freq = 0

        for i in range(len(arrival)):
            while used and used[0][0] <= arrival[i]:
                _, server = heapq.heappop(used)
                inc_list.add(server)

            if not inc_list:
                continue

            idx = inc_list.bisect_left(i % k)
            server = -1

            if idx < len(inc_list):
                server = inc_list[idx]
            else:
                server = inc_list[0]

            freq[server] += 1
            max_freq = max(max_freq, freq[server])

            inc_list.remove(server)

            heapq.heappush(used, (arrival[i] + load[i], server))

        for i, val in enumerate(freq):
            if val == max_freq and max_freq > 0:
                ans.append(i)

        return ans
