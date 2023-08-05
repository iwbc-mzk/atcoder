import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    G = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].add(b)

    no = [0] * N
    for n in range(1, N + 1):
        if no[n - 1] == -1:
            continue

        q = deque()
        q.append(n)
        visited = set()
        visited.add(n)
        while q:
            v = q.popleft()
            for vv in G[v]:
                no[vv - 1] = -1
                if vv in visited:
                    continue
                q.append(vv)
                visited.add(vv)

    ans = None
    for i in range(N):
        if no[i] == 0:
            if not ans:
                ans = i + 1
            else:
                print(-1)
                return
    print(ans)


if __name__ == "__main__":
    main()
