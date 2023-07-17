from itertools import permutations
from collections import defaultdict


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    XY = defaultdict(set)
    for _ in range(M):
        X, Y = map(int, input().split())
        XY[X].add(Y)
        XY[Y].add(X)

    MAX = 10**4 + 1

    ans = MAX
    for r in permutations(range(1, N + 1), N):
        t = 0
        for i, ri in enumerate(r):
            t += A[ri - 1][i]
            if i + 1 < N and r[i + 1] in XY[ri]:
                break
        else:
            ans = min(ans, t)

    print(ans if ans != MAX else -1)


if __name__ == "__main__":
    main()
