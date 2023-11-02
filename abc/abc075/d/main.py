import sys
from itertools import product


sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    X = [v[0] for v in XY]
    Y = [v[1] for v in XY]

    ans = float("inf")
    for x1, x2, y1, y2 in product(X, X, Y, Y):
        if x1 >= x2:
            continue
        if y1 >= y2:
            continue

        c = 0
        for x, y in XY:
            if x1 <= x <= x2 and y1 <= y <= y2:
                c += 1

        if c >= K:
            ans = min(ans, (x2 - x1) * (y2 - y1))

    print(ans)


if __name__ == "__main__":
    main()
