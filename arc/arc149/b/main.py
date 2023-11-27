import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = [(a, b) for a, b in zip(A, B)]
    AB.sort()

    B = [b for _, b in AB]

    INF = float("inf")
    dp = [INF for _ in range(N)]
    for b in B:
        i = bisect.bisect_right(dp, b)
        dp[i] = b

    lis_b = 0
    for v in dp:
        if v < INF:
            lis_b += 1

    print(N + lis_b)


if __name__ == "__main__":
    main()
