from collections import defaultdict
from math import inf
import heapq


def dijkstra(gragh, weights, start, N):
    visited = [False] * (N + 1)
    distances = [inf] * (N + 1)
    distances[start] = 0
    q = [(0, start)]
    while q:
        dist, v = heapq.heappop(q)
        if visited[v]:
            continue
        visited[v] = True
        for vv in gragh[v]:
            if visited[vv]:
                continue
            new_dist = dist + weights[v][vv]
            if new_dist < distances[vv]:
                distances[vv] = new_dist
                heapq.heappush(q, (new_dist, vv))
    return distances


def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    G = defaultdict(set)
    G_inv = defaultdict(set)
    C = defaultdict(lambda: defaultdict(int))
    C_inv = defaultdict(lambda: defaultdict(int))
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a].add(b)
        G_inv[b].add(a)
        C[a][b] = c
        C_inv[b][a] = c
    dist = dijkstra(G, C, 1, N)
    dist_inv = dijkstra(G_inv, C_inv, 1, N)
    ans = 0
    for n in range(1, N + 1):
        t = (T - dist[n] - dist_inv[n]) * A[n - 1]
        ans = max(ans, t)
    print(ans)


if __name__ == "__main__":
    main()
