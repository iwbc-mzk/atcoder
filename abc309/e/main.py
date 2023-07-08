from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())
    P = list(map(int, input().split()))

    G = defaultdict(set)
    for i, p in enumerate(P, 2):
        G[p].add(i)

    I = defaultdict(int)
    for _ in range(M):
        x, y = map(int, input().split())
        I[x] = max(I[x], y)

    visited = set()
    ans = 0
    for s in range(1, N + 1):
        if s in visited:
            continue

        i = I[s]
        if i == 0:
            continue

        q = deque()
        q.append((s, i + 1))
        visited.add(s)
        while q:
            v, vi = q.popleft()
            if vi > 0:
                ans += 1

            for vv in G[v]:
                if vv not in visited:
                    vii = max(vi - 1, I[vv] + 1 if I[vv] else 0)
                    q.append((vv, vii))
                    visited.add(vv)

    print(ans)


if __name__ == "__main__":
    main()
