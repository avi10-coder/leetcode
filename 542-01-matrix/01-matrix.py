from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        q = deque()
        result = [[-1] * n for _ in range(m)]

        # All zeros are sources
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    q.append((i, j))

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    if result[ni][nj] == -1:
                        result[ni][nj] = result[i][j] + 1
                        q.append((ni, nj))

        return result