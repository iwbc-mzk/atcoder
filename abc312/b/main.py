import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    blacks = [
        (0, 0),
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
        (6, 6),
        (7, 6),
        (8, 6),
        (6, 7),
        (6, 8),
        (7, 7),
        (7, 8),
        (8, 7),
        (8, 8),
    ]
    whites = [
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 2),
        (3, 1),
        (3, 0),
        (5, 5),
        (5, 6),
        (5, 7),
        (5, 8),
        (6, 5),
        (7, 5),
        (8, 5),
    ]

    ans = []
    for n in range(N):
        for m in range(M):
            ok = True
            for bn, bm in blacks:
                nn, mm = n + bn, m + bm
                if not (0 <= nn < N and 0 <= mm < M):
                    ok = False
                    break

                if S[nn][mm] != "#":
                    ok = False
                    break

            if not ok:
                continue

            for bn, bm in whites:
                nn, mm = n + bn, m + bm
                if S[nn][mm] != ".":
                    ok = False
                    break

            if ok:
                ans.append((n + 1, m + 1))

    ans.sort()
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
