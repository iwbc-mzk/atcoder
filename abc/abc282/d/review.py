from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())
    G = defaultdict(set)

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].add(v)
        G[v].add(u)

    colors = [0 for _ in range(N + 1)]
    S = []
    ans = 0
    for s in range(1, N + 1):
        if colors[s] != 0:
            continue

        c = 1
        colors[s] = c

        q = deque()
        q.append((s, c))

        g = {1: set(), -1: set()}
        g[c].add(s)
        l = 0
        while q:
            v, vc = q.popleft()
            for vv in G[v]:
                l += 1
                if colors[vv] == 0:
                    q.append((vv, -vc))
                    colors[vv] = -vc
                    g[-vc].add(vv)
                else:
                    if colors[vv] != -vc:
                        print(0)
                        return

        ans += len(g[1]) * len(g[-1]) - l // 2

        S.append(g)

    n = N * (N - 1) // 2
    for s in S:
        ss = len(s[1]) + len(s[-1])
        n -= ss * (ss - 1) // 2

    ans += n

    print(ans)


if __name__ == "__main__":
    main()
