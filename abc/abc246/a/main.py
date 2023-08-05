import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    X, Y = defaultdict(int), defaultdict(int)
    for _ in range(3):
        x, y = map(int, input().split())
        X[x] += 1
        Y[y] += 1

    for x, v in X.items():
        if v == 1:
            ansx = x
            break

    for y, v in Y.items():
        if v == 1:
            ansy = y
            break

    print(ansx, ansy)


if __name__ == "__main__":
    main()
