import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [float("inf")] * N
    dp[0] = 0

    for n in range(1, N):
        if n - 1 >= 0:
            dp[n] = min(dp[n], dp[n - 1] + abs(A[n] - A[n - 1]))
        if n - 2 >= 0:
            dp[n] = min(dp[n], dp[n - 2] + abs(A[n] - A[n - 2]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
