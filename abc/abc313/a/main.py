import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    P = list(map(int, input().split()))
    p1 = P[0]
    ans = 0
    for p in P[1:]:
        if p >= p1:
            ans = max(ans, p - p1 + 1)

    print(ans)


if __name__ == "__main__":
    main()
