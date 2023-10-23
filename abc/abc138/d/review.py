from collections import defaultdict, deque


def main():
    N, Q = map(int, input().split())
    G = defaultdict(set)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a].add(b)
        G[b].add(a)

    C = [0 for _ in range(N)]
    for _ in range(Q):
        p, x = map(int, input().split())
        C[p - 1] += x

    ans = [0 for _ in range(N)]
    q = deque()
    q.append((1, 0))
    visited = set()
    visited.add(1)
    while q:
        v, c = q.popleft()
        c += C[v - 1]
        ans[v - 1] = c
        for vv in G[v]:
            if vv not in visited:
                q.append((vv, c))
                visited.add(vv)

    print(*ans)


if __name__ == "__main__":
    main()
