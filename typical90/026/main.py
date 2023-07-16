from collections import defaultdict, deque


def dfs(s, N, G):
    ans = []

    q = deque()
    q.append((s, 0))
    visited = set()
    visited.add(s)
    while q:
        v, d = q.popleft()
        if d % 2 == 0:
            ans.append(v)
            if len(ans) == N // 2:
                break

        for vv in G[v]:
            if vv not in visited:
                q.append((vv, d + 1))
                visited.add(vv)

    return ans


def main():
    N = int(input())

    G = defaultdict(set)
    for _ in range(N - 1):
        A, B = map(int, input().split())
        G[A].add(B)
        G[B].add(A)

    ans = dfs(1, N, G)
    if len(ans) != N // 2:
        ans = dfs(G[1].pop(), N, G)

    print(*ans)


if __name__ == "__main__":
    main()
