class Solution:
    def countServers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        m = len(queries)
        ans: list[int] = [0] * m
        freq: list[int] = [0] * (n + 1)
        count = 0

        logs.sort(key=lambda a: a[1])
        qTime: list[list[int]] = []

        for i, query in enumerate(queries):
            qTime.append([query, i])

        qTime.sort(key=lambda a: a[0])

        i = 0
        j = 0

        for query, index in qTime:
            start = query - x
            end = query

            while j < len(logs) and logs[j][1] <= end:
                freq[logs[j][0]] += 1
                if freq[logs[j][0]] == 1:
                    count += 1
                j += 1

            while i < len(logs) and logs[i][1] < start:
                freq[logs[i][0]] -= 1
                if freq[logs[i][0]] == 0:
                    count -= 1
                i += 1

            ans[index] = n - count

        return ans
