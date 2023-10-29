import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    G = defaultdict(set)
    for _ in range(N - 1):
        A, B = map(int, input().split())
        G[A].add(B)
        G[B].add(A)

    visited = set()
    visited.add(1)
    q = deque()
    q.append(-1)
    q.append(1)
    k = [[] for _ in range(N)]
    # DFSの帰りがけ順で値を求めていく
    while q:
        v = q.pop()
        # 子の探索がすべて完了後に、全ての子のkと自分の値をマージしてソートする
        if v < 0:
            v = -v
            l = [X[v - 1]]
            for nv in G[v]:
                l += k[nv - 1]
            l.sort(reverse=True)
            k[v - 1] = l[:21]
            continue

        for nv in G[v]:
            if nv in visited:
                continue
            q.append(-nv)
            q.append(nv)
            visited.add(nv)

    for _ in range(Q):
        V, K = map(int, input().split())
        print(k[V - 1][K - 1])


if __name__ == "__main__":
    main()
