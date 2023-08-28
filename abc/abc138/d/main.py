import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    G = defaultdict(set)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a].add(b)
        G[b].add(a)

    I = [0] * (N + 1)
    for _ in range(Q):
        p, x = map(int, input().split())
        I[p] += x

    q = deque()
    q.append((1, I[1]))
    visited = set()
    visited.add(1)
    ans = [0] * N
    while q:
        v, d = q.pop()
        ans[v - 1] = d
        for vv in G[v]:
            if vv in visited:
                continue

            q.append((vv, d + I[vv]))
            visited.add(vv)

    print(*ans)


if __name__ == "__main__":
    main()
