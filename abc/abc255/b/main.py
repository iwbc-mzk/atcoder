import math


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    R = set(XY[a - 1] for a in A)
    NR = [xy for xy in XY if xy not in R]

    ans = 0
    for x1, y1 in NR:
        min_dist = math.inf
        for x2, y2 in R:
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            min_dist = min(min_dist, dist)

        if min_dist != math.inf:
            ans = max(ans, min_dist)

    print(math.sqrt(ans))


if __name__ == "__main__":
    main()
