import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    C = list(map(int, input().split()))

    gragh = defaultdict(set)
    for _ in range(N - 1):
        A, B = map(int, input().split())
        gragh[A].add(B)
        gragh[B].add(A)

    visited = set()
    q = deque()
    colors = [0] * 10**5

    visited.add(1)
    q.append(-1)
    q.append(1)

    ans = []
    while q:
        v = q.pop()

        if v < 0:
            colors[C[-v - 1] - 1] -= 1
            continue
        elif colors[C[v - 1] - 1] == 0:
            ans.append(v)

        colors[C[v - 1] - 1] += 1

        for nv in gragh[v]:
            if nv in visited:
                continue

            q.append(-nv)
            q.append(nv)
            visited.add(nv)

    for a in sorted(ans):
        print(a)


if __name__ == "__main__":
    main()
