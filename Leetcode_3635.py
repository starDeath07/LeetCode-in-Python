class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        INF = 10**10
        LW = INF
        WL = INF
        land = INF
        water = INF

        n, m = len(landStartTime), len(waterStartTime)

        for i in range(n):
            land = min(land, landStartTime[i] + landDuration[i])

        for i in range(m):
            water = min(water, waterStartTime[i] + waterDuration[i])
            LW = min(LW, max(land, waterStartTime[i]) + waterDuration[i])

        for i in range(n):
            WL = min(WL, max(water, landStartTime[i]) + landDuration[i])

        return min(WL, LW)
