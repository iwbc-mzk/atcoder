import sys
from itertools import permutations
from math import factorial

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    perms = permutations(range(N), N)
    dist = 0
    for perm in perms:
        for i in range(N - 1):
            x1, y1 = XY[perm[i + 1]]
            x2, y2 = XY[perm[i]]
            dist += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    print(dist / factorial(N))


if __name__ == "__main__":
    main()
