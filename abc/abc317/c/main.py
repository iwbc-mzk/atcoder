import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    G = defaultdict(set)
    D = [[-1] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        G[A].add(B)
        G[B].add(A)
        D[A][B] = C
        D[B][A] = C

    ans = 0
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        q = deque()
        q.append((i, 0))

        while q:
            v, d = q.pop()
            if v > 0:
                visited[v] = True
                ans = max(ans, d)
            else:
                visited[-v] = False
                continue

            for vv in G[v]:
                if not visited[vv]:
                    q.append((-vv, 0))
                    q.append((vv, d + D[v][vv]))

    print(ans)


if __name__ == "__main__":
    main()
