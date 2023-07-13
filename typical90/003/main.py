from collections import defaultdict, deque


def bfs(s, G):
    visited = set()

    q = deque()
    q.append((s, 0))
    visited.add(s)

    max_v = 0
    max_d = 0

    while q:
        v, d = q.popleft()
        if d > max_d:
            max_v = v
            max_d = d

        for vv in G[v]:
            if vv not in visited:
                q.append((vv, d + 1))
                visited.add(vv)

    return max_v, max_d


def main():
    N = int(input())

    G = defaultdict(set)
    for _ in range(N - 1):
        A, B = map(int, input().split())
        G[A].add(B)
        G[B].add(A)

    v, _ = bfs(1, G)
    _, ans = bfs(v, G)

    print(ans + 1)


if __name__ == "__main__":
    main()
