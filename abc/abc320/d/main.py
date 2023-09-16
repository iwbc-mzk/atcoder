import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    D = defaultdict(lambda: defaultdict(tuple))
    for _ in range(M):
        A, B, X, Y = map(int, input().split())
        D[A][B] = (X, Y)
        D[B][A] = (-X, -Y)

    ans = [None for _ in range(N)]
    ans[0] = (0, 0)
    q = deque()
    for key, val in D[1].items():
        q.append((1, key, val))

    u = set()
    u.add(1)
    while q:
        s, d, (x, y) = q.popleft()
        ans[d - 1] = (ans[s - 1][0] + x, ans[s - 1][1] + y)
        for key, val in D[d].items():
            if ans[key - 1] or key in u:
                continue
            q.append((d, key, val))
            u.add(key)

    for a in ans:
        if a:
            print(*a)
        else:
            print("undecidable")


if __name__ == "__main__":
    main()
