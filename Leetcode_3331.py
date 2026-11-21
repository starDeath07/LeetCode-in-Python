class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        adj: list[list[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        resultSize = [1] * n
        last = [-1] * 26

        def dfs(currNode: int):
            c = ord(s[currNode]) - ord("a")

            nearestAncestor = last[c]
            last[c] = currNode

            for child in adj[currNode]:
                dfs(child)

            last[c] = nearestAncestor

            if currNode != 0:
                newParent = parent[currNode]

                if nearestAncestor != -1:
                    newParent = nearestAncestor

                parent[currNode] = newParent
                resultSize[newParent] += resultSize[currNode]

        dfs(0)
        return resultSize
