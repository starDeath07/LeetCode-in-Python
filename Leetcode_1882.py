import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = []
        inuse = []

        for i in range(len(servers)):
            free.append((servers[i], i))

        heapq.heapify(free)
        res = []

        for i, t in enumerate(tasks):
            while inuse and inuse[0][0] <= i:
                heapq.heappush(free, heapq.heappop(inuse)[1:])

            far = 0

            if not free:
                far, w, j = heapq.heappop(inuse)
                heapq.heappush(free, (w, j))

            w, j = heapq.heappop(free)
            heapq.heappush(inuse, (max(i, far) + t, w, j))
            res.append(j)

        return res
