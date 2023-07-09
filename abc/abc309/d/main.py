from collections import defaultdict, deque


def main():
    N1, N2, M = map(int, input().split())

    G = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].add(b)
        G[b].add(a)

    ans = 0
    for s in [1, N1 + N2]:
        q = deque()
        q.append((s, 0))
        visited = set()
        visited.add(s)
        max_d = 0
        while q:
            v, d = q.popleft()
            for vv in G[v]:
                if vv not in visited:
                    q.append((vv, d + 1))
                    max_d = max(max_d, d + 1)
                    visited.add(vv)

        ans += max_d

    print(ans + 1)


if __name__ == "__main__":
    main()
