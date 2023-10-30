import sys
from collections import defaultdict
import heapq

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    G = defaultdict(set)
    Ginv = defaultdict(set)
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].add(B)
        Ginv[B].add(A)

    ans = []
    S = []
    for i in range(1, N + 1):
        if i not in Ginv:
            heapq.heappush(S, i)

    while S:
        v = heapq.heappop(S)
        ans.append(v)
        for nv in G[v]:
            Ginv[nv].remove(v)
            if not Ginv[nv]:
                heapq.heappush(S, nv)

    for e in Ginv.values():
        if e:
            print(-1)
            return

    print(*ans)


if __name__ == "__main__":
    main()
