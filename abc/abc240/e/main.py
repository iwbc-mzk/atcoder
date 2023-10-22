import sys
from collections import deque, defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    G = defaultdict(set)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u].add(v)
        G[v].add(u)

    LR = [None for _ in range(N)]
    q = deque()
    q.append(-1)
    q.append(1)
    visited = set()
    visited.add(1)
    t = 1
    INF = float("inf")
    while q:
        v = q.pop()
        if v < 0:
            v = -v
            l, r = INF, -INF
            for vv in G[v]:
                if LR[vv - 1] is None:
                    continue
                else:
                    ll, rr = LR[vv - 1]
                    l = min(l, ll)
                    r = max(r, rr)

            if l == INF and r == -INF:
                l, r = t, t
                t += 1

            LR[v - 1] = (l, r)
            continue

        for vv in G[v]:
            if vv in visited:
                continue

            q.append(-vv)
            q.append(vv)
            visited.add(vv)

    for lr in LR:
        print(*lr)


if __name__ == "__main__":
    main()
