import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    G = defaultdict(set)
    for a, b in AB:
        G[a].add(b)
        G[b].add(a)

    ans = 0
    for a, b in AB:
        visited = set()
        visited.add(1)
        q = deque()
        q.append(1)

        while q:
            v = q.popleft()
            for nv in G[v]:
                if (v == a and nv == b) or (v == b and nv == a):
                    continue

                if nv in visited:
                    continue

                q.append(nv)
                visited.add(nv)

        if len(visited) != N:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
