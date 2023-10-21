import sys

sys.setrecursionlimit(10**9)
from collections import defaultdict
from math import inf
import heapq


def main():
    N, A, B, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(N)]

    start = 1
    visited = set()
    distances1 = defaultdict(lambda: inf)
    distances1[start] = 0

    q = [(0, start)]
    while q:
        # 未処理の中で最小の距離を持つ頂点を取り出す
        dist, v = heapq.heappop(q)
        if v in visited:
            continue

        visited.add(v)

        for vv in range(1, N + 1):
            if vv in visited:
                continue

            new_dist = dist + D[v - 1][vv - 1] * A
            if new_dist < distances1[vv]:
                distances1[vv] = new_dist
                heapq.heappush(q, (new_dist, vv))

    start = N
    visited = set()
    distances2 = defaultdict(lambda: inf)
    distances2[start] = 0

    q = [(0, start)]
    while q:
        # 未処理の中で最小の距離を持つ頂点を取り出す
        dist, v = heapq.heappop(q)
        if v in visited:
            continue

        visited.add(v)

        for vv in range(1, N + 1):
            if vv in visited:
                continue

            new_dist = dist + D[v - 1][vv - 1] * B + C
            if new_dist < distances2[vv]:
                distances2[vv] = new_dist
                heapq.heappush(q, (new_dist, vv))

    ans = float("inf")
    for i in range(1, N + 1):
        ans = min(ans, distances1[i] + distances2[i])

    print(ans)


if __name__ == "__main__":
    main()
