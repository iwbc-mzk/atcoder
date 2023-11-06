import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    G = defaultdict(set)
    for a, b in zip(A, B):
        G[a].add(b)
        G[b].add(a)

    X = [-1] * (N + 1)
    finished = set()
    for i in range(1, N + 1):
        if i in finished:
            continue

        q = deque()
        q.append((i, 0))
        finished.add(i)
        X[i] = 0
        while q:
            v, d = q.popleft()
            nd = 1 if d == 0 else 0
            for nv in G[v]:
                if X[nv] != -1 and nd != X[nv]:
                    print("No")
                    return
                else:
                    if nv not in finished:
                        X[nv] = nd
                        q.append((nv, nd))
                        finished.add(nv)

    print("Yes")


if __name__ == "__main__":
    main()
