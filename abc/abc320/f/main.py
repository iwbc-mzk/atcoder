import sys
from itertools import combinations

sys.setrecursionlimit(10**9)


def main():
    N, H = map(int, input().split())
    X = list(map(int, input().split()))
    PF = [tuple(map(int, input().split())) for _ in range(N - 1)]

    ans = float("inf")
    for i, j in combinations(range(N - 1), 2):
        if i == j:
            continue

        for x, y in [(i, j), (j, i)]:
            a = 0
            h = H
            p = 0
            for k in range(N - 1):
                if h >= (X[k] - p):
                    h -= X[k] - p
                    p = X[k]
                else:
                    break

                if k == x:
                    h = min(H, h + PF[k][1])
                    a += PF[k][0]
            else:
                if h < (X[-1] - p):
                    break

                h -= X[-1] - p
                p = X[-1]
                for k in reversed(range(N - 1)):
                    if h >= (p - X[k]):
                        h -= p - X[k]
                        p = X[k]
                    else:
                        break

                    if k == y:
                        h = min(H, h + PF[k][1])
                        a += PF[k][0]
                else:
                    ans = min(ans, a)

    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
