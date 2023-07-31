from collections import defaultdict, deque
from math import inf


def bfs_dist(s, G, D, N):
    q = deque()
    q.append((s, 0))
    dis = [inf for _ in range(N)]
    dis[s - 1] = 0
    visited = [inf for _ in range(N)]
    while q:
        v, d = q.popleft()
        if visited[v - 1] <= d:
            continue
        else:
            visited[v - 1] = d

        for vv in G[v]:
            dd = d + D[v][vv]
            if dd < dis[vv - 1]:
                dis[vv - 1] = dd
                q.append((vv, dd))

    return dis


def main():
    N, M = map(int, input().split())

    G = defaultdict(set)
    D = defaultdict(lambda: defaultdict(int))

    for _ in range(M):
        A, B, C = map(int, input().split())
        G[A].add(B)
        G[B].add(A)
        D[A][B] = C
        D[B][A] = C

    dist1 = bfs_dist(1, G, D, N)
    distN = bfs_dist(N, G, D, N)

    for i in range(1, N + 1):
        print(dist1[i - 1] + distN[i - 1])


if __name__ == "__main__":
    main()
