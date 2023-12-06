from collections import defaultdict, deque


def bfs(gragh, C, N):
    visited = set()
    q = deque()
    q.append((1, N, 0))
    visited.add((1, N))
    dist = -1

    while q:
        t, a, d = q.popleft()
        if t == N and a == 1:
            dist = d
            break

        for nt in gragh[t]:
            for na in gragh[a]:
                if C[nt - 1] == C[na - 1]:
                    continue

                if (nt, na) in visited:
                    continue

                q.append((nt, na, d + 1))
                visited.add((nt, na))

    return dist


def main():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        C = list(map(int, input().split()))

        gragh = defaultdict(set)
        for _ in range(M):
            u, v = map(int, input().split())
            gragh[u].add(v)
            gragh[v].add(u)

        if C[0] == C[N - 1]:
            print(-1)
            continue

        ans = bfs(gragh, C, N)
        print(ans)


if __name__ == "__main__":
    main()
